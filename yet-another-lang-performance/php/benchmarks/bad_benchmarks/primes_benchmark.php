<?php
    namespace Benchmarks\BadBenchmarks;
    include dirname(__FILE__).'/../benchmark.php';

    use Benchmarks\Benchmark;

    class PrimesBenchmark extends Benchmark{

        const MAX_PRIME = 10000000;

        function __construct() {
            parent::__construct("Bad primes example");
        }

        private function get_primes7($n) {
            if ($n < 2) return array();
            if ($n == 2) return array(2);
            $s = range(3, $n, 2);
            $mroot = sqrt($n);
            $half = count($s);
            $i = 0;
            $m = 3;
            while ($m <= $mroot) {
                if ($s[$i]) {
                    $j = (int)(($m*$m - 3) / 2);
                    $s[$j] = 0;
                    while ($j < $half) {
                        $s[$j] = 0;
                        $j += $m;
                    }
                }
                $i = $i + 1;
                $m = 2*$i + 3;
            }
            $res = array(2);
            foreach ($s as $v) {
                if ($v) {
                    $res[] = $v;
                }
            }
            return $res;
        }
        
        protected function execute_impl(){
            return $this->get_primes7(self::MAX_PRIME);
        }
    }
    
?>