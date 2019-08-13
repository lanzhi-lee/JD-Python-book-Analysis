// 插件使用示例
$(document).ready(function() {
    $(this)._naiveScroll.init();
    $('#upBtn').click(function () {
        $(this)._naiveScroll.triggerScroll(100);
    });
    $('#downBtn').click(function () {
        $(this)._naiveScroll.triggerScroll(-100);
    });
});
