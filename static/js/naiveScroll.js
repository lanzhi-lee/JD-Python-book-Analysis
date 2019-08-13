/**
 * Created by yfwang14 on 16/7/20.
 */
!function($) {
    $.fn._naiveScroll = {
        lastAnimationTime: new Date().getTime()
    };

    /**
     * 添加默认 section 属性并监听滚轮事件
     */
    $.fn._naiveScroll.init = function() {
        $('section:first').addClass('active');
        $(document).bind('mousewheel DOMMouseScroll', function(event) {
            event.preventDefault();
            var delta = event.originalEvent.wheelDelta || -event.originalEvent.detail;
            $(this)._naiveScroll.triggerScroll(delta);
        });
    };

    /**
     * 根据当前位置和滚动方向, 设置滚动后的 active 位置
     * @param {int} currentActive - 当前 section 序号
     * @param {string} direction - 滚动方向
     */
    $.fn._naiveScroll.setActiveSection = function(currentActive, direction) {
        var sections = $('section');
        var newActive = direction === 'down' ? currentActive + 1 : currentActive - 1;
        // console.log("now: " + currentActive);
        // console.log("new: " + newActive);
        sections.each(function(index, element) {
            $(element).removeClass('active');
            if (index == newActive) {
                $(element).addClass('active');
            }
        });
        sections.each(function(index, element) {
            if (index == newActive) {
                $(element).addClass('active');
            }
        });
    };

    /**
     * 获得下一次滚动位置的百分比
     * @param {string} direction - 滚动方向
     * @returns {number}
     */
    $.fn._naiveScroll.getPercentage = function(direction) {
        var sections = $('section');
        var activeSection = 0;
        sections.each(function(index, element) {
            if ($(element).hasClass('active')) {
                activeSection = index;
            }
        });
        if (direction === 'up') {
            if (activeSection == 0) {
                return 0;
            }
            else {
                $(this)._naiveScroll.setActiveSection(activeSection, direction);
                return -100 * (activeSection - 1);
            }
        } else if (direction === 'down') {
            if (activeSection == sections.length - 1) {
                return -100 * activeSection;
            }
            else {
                $(this)._naiveScroll.setActiveSection(activeSection, direction);
                return -100 * (activeSection + 1);
            }
        } else {
            return 0;
        }
    };

    /**
     * 执行滚动动作
     * @param {string} direction - 滚动方向
     */
    $.fn._naiveScroll.transformPage = function(direction) {
        console.log('transform performed');
        $(this)._naiveScroll.lastAnimationTime = new Date().getTime();
        var percentage = $(this)._naiveScroll.getPercentage(direction);
        $("section").css({
            "transform": "translate(0, " + percentage + "%)",
            "transition": "all 1000ms ease"
        });
    };

    /**
     * 滚动触发器, 根据事件时间判断是否执行滚动动作
     * @param {int} delta - 浏览器滚动事件的距离
     */
    $.fn._naiveScroll.triggerScroll = function(delta) {
        var timeNow = new Date().getTime();
        if (timeNow - $.fn._naiveScroll.lastAnimationTime < 1500) {
            return;
        }
        var direction = delta < 0 ? 'down' : 'up';
        $(this)._naiveScroll.transformPage(direction);
    }
}(window.jQuery);
