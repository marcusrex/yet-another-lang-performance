<?php
    namespace Benchmarks;

    class BenchmarkStat {
        public $name;
        public $avg_elapsed_time;
        public $run_number;
        public $used_mem;
        public $total_used_mem;

        function __construct($name, $avg_elapsed_time, $used_mem, $total_used_mem,  $run_number) {
            $this->name = $name;
            $this->avg_elapsed_time = $avg_elapsed_time;
            $this->run_number = $run_number;
            $this->used_mem = $used_mem;
            $this->total_used_mem = $total_used_mem;
        }
    }

    abstract class Benchmark {
        protected $name;

        const RETRY_NUMBER = 1;

        function __construct($name) {
                $this->name = $name;
        }

        protected abstract function execute_impl();

        public function execute() {
            $times = array();
            foreach (range(1, self::RETRY_NUMBER) as $number) {
                $start = microtime(true);
                $this->execute_impl();
                $end = microtime(true);
                array_push($times, $end - $start);
            }

            $memories = array();
            $total_memories = array();          

            foreach (range(1, self::RETRY_NUMBER) as $number) {
                $start_mem = memory_get_usage();
                $res = $this->execute_impl();
                $end_mem = memory_get_usage();
                array_push($total_memories, ((memory_get_usage(True))/pow(2,20)));
                unset($res);
                array_push($memories, (($end_mem - $start_mem)/pow(2,20)));
            }

            return new BenchmarkStat($this->name, array_sum($times)/self::RETRY_NUMBER, array_sum($memories)/self::RETRY_NUMBER,array_sum($total_memories)/self::RETRY_NUMBER, self::RETRY_NUMBER);

        }
    }
?>