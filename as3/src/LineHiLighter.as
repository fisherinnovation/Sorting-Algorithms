package {
	import flash.display.Sprite;

	public class LineHiLighter extends Sprite {
		
		private var _line:Sprite;
		
		
		/**
		 * 
		 */
		public function LineHiLighter() {
			init();
		}
		
		
		/**
		 * 
		 */
		private function init():void {
			_line = new Sprite();
			_line.graphics.beginFill(0xFF0000);
			_line.graphics.drawRect(0, 0, 600, 1);
			_line.graphics.endFill();
			addChild(_line);
		}
	}
}