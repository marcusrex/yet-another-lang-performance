<?php
    namespace Benchmarks;

    class BenchmarkStat {
        public $name;
        public $avg_elapsed_time;
        public $run_number;

        function __construct($name, $avg_elapsed_time, $run_number) {
            $this->name = $name;
            $this->avg_elapsed_time = $avg_elapsed_time;
            $this->run_number = $run_number;
        }
    }

    abstract class Benchmark {
        protected $name;

        const RETRY_NUMBER = 100;

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

            return new BenchmarkStat($this->name, array_sum($times)/self::RETRY_NUMBER, self::RETRY_NUMBER);

        }
    }
?>