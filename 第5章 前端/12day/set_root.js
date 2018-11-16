(function(){
	var calc = function(){
		var docElement = document.documentElement; //获取html标签的元素
		// 客户端宽度
		// var clientWidthValue = docElement.clientWidth > 750 ? 750 : docElement.clientWidth;
		var clientWidthValue
		if(docElement.clientWidth > 750){
			clientWidthValue=750;
		}
		else
		{
			clientWidthValue = docElement.clientWidth;
		}

		docElement.style.fontSize = 20*(clientWidthValue/375) + 'px';
	}

	calc();//一进来就运行一次  跟定时器那里同理
	// 绑定一个监听 当resize 窗口宽度发生改变时  就调用calc
	window.addEventListener('resize',calc);
})();