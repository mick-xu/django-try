/* Write here your custom javascript codes */

$(function () {
    var marqueeScroll = function (id1, id2, id3, timer) {
        var $parent = $("#" + id1);
        var $goal = $("#" + id2);
        var $closegoal = $("#" + id3);
        $closegoal.html($goal.html());

        function Marquee() {
            if (parseInt($parent.scrollLeft()) - $closegoal.width() >= 0) {
                $parent.scrollLeft(parseInt($parent.scrollLeft()) - $goal.width());
            } else {
                $parent.scrollLeft($parent.scrollLeft() + 1);
            }
        }

        setInterval(Marquee, timer);
    }
    var marqueeScroll1 = new marqueeScroll("marquee-box", "wave-list-box1", "wave-list-box2", 20);
    var marqueeScroll2 = new marqueeScroll("marquee-box3", "wave-list-box4", "wave-list-box5", 40);

    $(".official-plat ul li").hover(function () {
        if ($(this).index() == 0) {
            $(".weixin").show();
            $(".weibo").hide();
        } else {
            $(".weixin").hide();
            $(".weibo").show();
        }

    });

    $(".tabs .tab-nav").on("click", "li", function () {
        $(this).addClass("active").siblings("li").removeClass("active").parent(".tab-nav").nextAll(".tab-panel").children(".list").eq($(this).index()).show().siblings(".list").hide();
    });
})