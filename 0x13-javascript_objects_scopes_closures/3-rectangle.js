#!/usr/bin/node

/**
 * A rectangle class with parameteres provided
 */

class Rectangle(){
	constructor(w, h){
		if(typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0){
			this.width = w;
			this.height = h;
		}
	}

	print(){
		for(i = 0; i < this.height; i++){
			let myVar = '';
			let y = 0;
			while(y < this.width){
				myVar += 'x';
				y++;
			}
			console.log(myVar);
		}
	}
}
module.exports = Rectangle;
