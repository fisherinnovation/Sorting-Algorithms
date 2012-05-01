<?php

	/**
	 * Sorting Algorithm Examples in PHP
	 * 
	 * Matt Fisher - http://www.fisherinnovation.com
	 * Github - https://github.com/fisherinnovation/Sorting-Algorithms
	 */

 
	$n = 1000; 				// Number of elements to sort.
	$sortlist = array();	// List of intergers.

	for($i = 0; $i < $n; $i++) array_push($sortlist, $i);
	
	
	/**
	 * Randomizes the lists of integers.
	 */
	function randomizeList() {
		global $sortlist;
		shuffle($sortlist);
	}
	
	
	/**
	 * Bubble Sort
	 */
	function bubbleSort($arr) {
		$time_begin = microtime(true);
		$size = count($arr);
	    for ($i=0; $i<$size; $i++) {
	        for ($j=0; $j<$size-1-$i; $j++) {
	            if ($arr[$j+1] < $arr[$j]) {
	                swap($arr, $j, $j+1);
	            }
	        }
	    }
		
		$time_end = microtime(true) - $time_begin;
		echo 'Bubble Sort: ' . $time_end . ' seconds.<br>';
	}
	
	
	/**
	 * Swaps two elements in a array.
	 * Used by Bubble Sort.
	 */
	function swap(&$arr, $a, $b) {
	    $tmp = $arr[$a];
	    $arr[$a] = $arr[$b];
	    $arr[$b] = $tmp;
	}
	
	
	/**
	 * Sort an array and maintain index association.
	 * Uses PHP asort.
	 */
	function associativeSort($list) {
		$time_begin = microtime(true);
		asort($list);
		$time_end = microtime(true) - $time_begin;
		echo 'Associative Sort: ' . $time_end . ' seconds.<br>';
	}
	
	
	/**
	 * Sort an array by key
	 * Uses PHP ksort.
	 */
	function keySort($list) {
		$time_begin = microtime(true);
		ksort($list);
		$time_end = microtime(true) - $time_begin;
		echo 'Key Sort: ' . $time_end . ' seconds.<br>';
	}
	
	
	/**
	 * Insertion Sort.
	 */
	function insertionSort($list) {
		$time_begin = microtime(true);
		
	    $l = sizeof($list);
		
		for($i = 0; $i < $l; $i++) {
	        $save = $list[$i];
	        $j = $i;
			
	        while($j > 0 && $list[$j - 1] > $save) {
	            $list[$j] = $list[$j - 1];
	            $j -= 1;
			}
	        
	        $list[$j] = $save;
		}
		
		$time_end = microtime(true) - $time_begin;
		echo 'Insertion Sort: ' . $time_end . ' seconds.<br>';
	}
	
	
	
	print "Benchmarking Sorting Algorithms <br>" . $n . " randomized integers<hr/>";
	randomizeList();
	bubbleSort($sortlist);
	randomizeList();
	associativeSort($sortlist);
	randomizeList();
	keySort($sortlist);
	randomizeList();
	insertionSort($sortlist);
	
?>