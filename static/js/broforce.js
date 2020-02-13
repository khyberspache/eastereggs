
/** VOICE **/

controls = [
    {
        'broforce': displayBROFORCE
    }
]
activate(controls);

function displayBROFORCE() {
	$('.logo-container').css('display', 'block');
	$('.big-head').css('display', 'none');
}

/// JS from http://www.broforcegame.com, thanks y'all, this is awesome

// on-init
$(document).ready( function() {
	
	// various explosions
	setInterval(function() { explode(0); explode(500) }, 1000);
});

// explosion list
var explosionCount = 0;
function explosions(count, interval)
{
	for (var i = 0; i < count; i ++)
	{
		explode(i * interval);
	}

	setTimeout(function() { shakeLogo(50); }, 0);
}

// actual explosions
function explode(delay)
{
	if (window.innerWidth > 900)
	{
		setTimeout(function()
		{
			explosionCount ++;

			var index = explosionCount;
			var parent = $("#explosions");
			var positionX = Math.random() * 800;
			var positionY = Math.random() * 400;
			var explosionType = (Math.random() < 0.25 ? 2 : 1);

			parent.append("<div class='explosion" + explosionType + "' style='left:" + positionX + "px; top:" + positionY + "px;' id='explosion-" + index +"'>&nbsp;</div>")
			setTimeout(function() { $("#explosion-" + index).remove(); }, 1000);
		}, delay);
	}
}

// shakes the logo
function shakeLogo(count)
{
	count --;
	if (count > 0)
	{
		var padding = (-25 + Math.random() * 50) * (count / 50);
		$("#logo").css("margin-left", (-50 + Math.random() * 100) * (count / 50) +"px");
		$("#logo").css("margin-top", padding + "px");
		$("#logo").css("margin-bottom", (-padding) + "px");
		setTimeout(function() { shakeLogo(count); }, 10);
	}
	else
	{
		$("#logo").css("margin-left", "0px");
		$("#logo").css("margin-top", "0px");
		$("#logo").css("margin-bottom", "0px");
	}
}
