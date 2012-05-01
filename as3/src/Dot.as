package {
	import flash.display.Sprite;

	public class Dot extends Sprite {
		
		public var _value:int = 0;
		
		/**
		 * Dot Constructor
		 */
		public function Dot() {
			init();
		}
		
		
		/**
		 * Creates the dot.
		 */
		private function init():void {
			var n:Sprite = new Sprite();
			n.graphics.beginFill(0x000000);
			n.graphics.drawRect(0, 0, 1, 1);
			n.graphics.endFill();
			addChild(n);
		}
		
		
		public function getValue():int { return _value; }
		public function setValue($val:int):void { _value = $val; }
	}
}