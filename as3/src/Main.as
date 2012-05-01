package
{
	import com.greensock.TweenLite;
	
	import flash.display.Sprite;
	
	[SWF(frameRate="60", backgroundColor="0xFFFFFF", width="600", height="600")]
	public class Main extends Sprite {
		
		private var _list:		Array;
		private var _amount:	int = 600;
		private var _line:LineHiLighter;
		
		/**
		 * 
		 */
		public function Main() {
			init();
			insertionSort(_list);
		}
		
		
		/**
		 * 
		 */
		private function init():void {
			_list = new Array();
			
			// Background line.
			_line = new LineHiLighter();
			addChild(_line);
			
			for(var i:int = 0; i < _amount; i++) {
				var dot:Dot = new Dot();
				dot.setValue(i);
				dot.x = i;
				dot.y = i;
				addChild(dot);
				_list.push(dot);
			}
			
			arrayShuffle();
		}
		
		
		/**
		 * 
		 */
		private function arrayShuffle():void {
			// Shuffle array
			for(var i:int = 0; i < _list.length; i++){
				var randomNum_num:Number = Math.floor(Math.random() * _list.length)
				var arrayIndex:Dot = _list[i];
				_list[i] = _list[randomNum_num];
				_list[randomNum_num] = arrayIndex;
			}
			
			// Update dot positions
			for(i = 0; i < _list.length; i++) {
				_list[i].x = i;
			}
		}
		
		
		/**
		 * Insertion Sort.
		 * 
		 * @param	$list	The array to sort.
		 */
		private function insertionSort($list:Array):void {
			var l:int = $list.length;
			
			for(var i:int = 0; i < l; i++) {
				var save:Dot = $list[i];
				var j:int = i;
				
				while(j > 0 && $list[j - 1].getValue() > save.getValue()) {
					$list[j] = $list[j - 1];
					j -= 1;
				}
				
				$list[j] = save;
				_list = $list;
				
				// Animate the item into proper position.
				TweenLite.to($list[j], 0.25, { onStart:moveLine, onStartParams:[$list[j].getValue()], x:$list[j].getValue(), delay:i * 0.01 });
			}
		}
		
		
		/**
		 * Move the line to the active sort.
		 * 
		 * @param	$y	Where to move the line to.
		 */ 
		private function moveLine($y:int):void {
			_line.y = $y;
		}
		
	}
}