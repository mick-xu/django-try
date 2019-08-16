var RevolutionSlider = function () {

	return {

		//Revolution Slider - Full Width
		initRSfullWidth: function () {
			var revapi;
			jQuery(document).ready(function () {
				revapi = jQuery('.tp-banner').revolution({
					delay: 9000,
					startwidth: 1170,
					startheight: 420,
					fullWidth: "on",
					dottedOverlay: "none",
					shadow: 0,
					spinner: 'spinner5',
					hideTimerBar: 'on',
					navigationType: "bullet",
					navigationArrows: "solo",
					navigationStyle: "round",
				});
			});
		},

		//Revolution Slider - Full Screen Offset Container
		initRSfullScreenOffset: function () {
			var revapi;
			jQuery(document).ready(function () {
				revapi = jQuery('.tp-banner').revolution({
					delay: 15000,
					startwidth: 1170,
					startheight: 400,
					hideThumbs: 10,
					fullWidth: "off",
					fullScreen: "on",
					hideCaptionAtLimit: "",
					dottedOverlay: "twoxtwo",
					navigationStyle: "preview4",
					fullScreenOffsetContainer: ".header"
				});
			});
		}

	};
}();