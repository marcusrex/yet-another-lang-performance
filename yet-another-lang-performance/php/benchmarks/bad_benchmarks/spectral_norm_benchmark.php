<?php
    namespace Benchmarks\BadBenchmarks;
    require_once(dirname(__FILE__).'/../benchmark.php');

    use Benchmarks\Benchmark;

    class SpectralNormBenchmark extends Benchmark{

        const MAX_SPEC = 5500;

        function __construct() {
            parent::__construct("Bad spectral example");
        }

        private function get_spec($n) {
            $u = array_fill(0, $n, 1.0);
            $_tpl = array_fill(0, $n, 0.0);
            $v = $this->AtAv($n,$u,0,$n);
            $u = $this->AtAv($n,$v,0,$n);
            $vBv = 0.0;
            $vv = 0.0;
            $i = 0;
            foreach($v as $val) {
               $vBv += $u[$i]*$val;
               $vv += $val*$val;
               ++$i;
            }
            
            return sqrt($vBv/$vv);
        }

        function A($i, $j){
            return 1.0 / ( ( ( ($i+$j) * ($i+$j+1) ) >> 1 ) + $i + 1 );
         }
         
         function Av($n, $v, $start, $end){
            global $_tpl;
            $Av = $_tpl;
            for ($i = $start; $i < $end; ++$i) {
               $sum = 0.0;
               foreach($v as $j=>$v_j) {
                  $sum += $this->A($i,$j) * $v_j;
               }
               $Av[$i] = $sum;
            }
            return $Av;
         }
         
         function Atv($n, $v, $start, $end){
            global $_tpl;
            $Atv = $_tpl;
            for($i = $start; $i < $end; ++$i) {
               $sum = 0.0;
               foreach($v as $j=>$v_j) {
                  $sum += $this->A($j,$i) * $v_j;
               }
               $Atv[$i] = $sum;
            }
            return $Atv;
         }
         
         function AtAv($n, $v, $start, $end){       
            $tmp = $this->Av($n, $v, $start, $end);       
            $tmp = $this->Atv($n, $tmp, $start, $end);
         
            return $tmp;
         }
        
        protected function execute_impl(){
            return $this->get_spec(self::MAX_SPEC);
        }
    }
    
?>