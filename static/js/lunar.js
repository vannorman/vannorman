/*
* epsioln schedule
*/
/* from
https://github.com/puresick/Lunar-Lander/
*/




var state = {
    input : {
        up : false,
        down : false,
        left : false,
        right : false
 
    }, momentum : {
        x : 0,
        y : 0
    }, fuel : 300,
    position : {
      x : 0,
      y : 0,
    }, target : {
      x : 0,
      y : 0,
    }
}




$(document).keydown((key) => {
//    console.log("key rep:"+key.repeat);
switch (key.keyCode) {
    case 87: //UP (w)
      state.input.up = true;
      break;
    case 83: //DOWN (s)
      state.input.down = true;
      break;
    case 65: //LEFT (a)
      state.input.left= true;
      break;
    case 68: //RIGHT (d)
      state.input.right = true;
      break;
  }
});


$(document).keyup((key) => {
   switch(key.keyCode){
    case 87: //UP (w)
        state.input.up = false;
    break;
    case 83: //DOWN (s)
        state.input.down = false;
      break;
    case 65: //LEFT (a)
        state.input.left = false;
      break;
    case 68: //RIGHT (d)
        state.input.right = false;
      break;
  }
 
});


socket = null;
function SocketTest(){
    /* SOCKETS */
    socket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/msg/');

    var testSocket = new WebSocket("ws://echo.websocket.org/")

    // receive
    socket.onmessage = function(e) {
      console.log(e)
        var data = JSON.parse(e.data);
        var message = data['message'];
        
    };

     socket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };  
    console.log('connecting!');

    var message = "message!";
    socket.onopen = () => {
      console.log('opened!!');

      socket.send(JSON.stringify({
          'message': message
      }));
    }
}















// I want to create a list of vector8s, like [{"a":a,"b":b,,,"8":9},{"a":2,"b":3, ..}, ... {}]

currentSessionData = []


function GameLoop(dt){
    setTimeout(function(){GameLoop(dt);},dt);
    var power = .003;
    var consumption = .05;
    var yDir = 0;
    var xDir = 0;
    var momentumDecay = .005;
    if (state.input.up){
        yDir = -1;
        state.momentum.y -= power;
        state.fuel = state.fuel - consumption;
    } else if (state.input.down){
        yDir = 1;
        state.momentum.y += power;
        state.fuel = state.fuel - consumption;
        
    } else if (state.input.right){
        xDir = 1;
        state.momentum.x += power;
        state.fuel = state.fuel - consumption;
    
    } else if (state.input.left) {
        xDir = -1;
        state.momentum.x -= power;
        state.fuel = state.fuel - consumption;
    }
    state.position.y = state.position.y + state.momentum.y;
    state.position.x = state.position.x + state.momentum.x;

    state.momentum.x = lerp(state.momentum.x, 0, momentumDecay);
    state.momentum.y = lerp(state.momentum.y, 0, momentumDecay);

    

    
    currentSessionData.push(state);
    
}

var lerp =  function (value1, value2, amount) {
    amount = amount < 0 ? 0 : amount;
    amount = amount > 1 ? 1 : amount;
    return value1 + (value2 - value1) * amount;
}



function InitTarget(){
   state.target.x =  $('#platform').offset().left;
    state.target.y =  $('#platform').offset().top; // - $('#platform').height();
}

$(document).ready(() => {
  InitTarget();
    GameLoop();
  function drawGame() {
    //distance calculation between player and platform

    //checking for game over cases
    if (
      state.position.y >= $(window).height()
        - parseFloat($('#lander').css('height'))
        - parseFloat($('#ground').css('height')) ||
      state.position.x >= $(window).width() - 20 ||
      state.position.x < 0 ||
      state.fuel <= 0
    ) {
      $('#gameover')
        .css({'display': 'block', 'background-color': '#f00'}).text('GAME OVER');
      clearInterval(drawGameId);
    };

    //checking for win case
    if (
      state.position.x - state.target.x >= 0 &&
      state.position.x - state.target.x <= parseFloat($('#platform').css('width')) &&
      Math.abs(state.position.y + $('#lander').height() - state.target.y) < 2 &&
      state.momentum.x + state.momentum.y < .5
    ) {
      $('#gameover').css({'display': 'block', 'background-color': '#0f0'}).text('YOU WIN');
      clearInterval(drawGameId);
    }
    // console.log("x,y:"+state.position.x.toFixed(2)+", "+state.position.y.toFixed(2)+" -- target;"+state.target.x.toFixed(2)+", "+state.target.y.toFixed(2));
    // calculation of player movement incl. gravity and amount of state.fuel 
    $('#lander').css({
      'top': () => {
        state.position.y = state.position.y + 0.18;
        return state.position.y;
      },
      'left': () => {
        return state.position.x;
      }
    });
    // $('#fuel').text('FUEL: ' + state.fuel.toFixed(2)); //+", momentum:"+state.momentum.x.toFixed(2)+", "+state.momentum.y.toFixed(2));
    $('#fuel').text('FUEL: ' + state.fuel.toFixed(2)+", momentum:"+state.momentum.x.toFixed(2)+", "+state.momentum.y.toFixed(2));
  };
  //drawing game at 30fps
  const drawGameId = setInterval(drawGame, 0.03);
});
