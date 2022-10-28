
var player;
var players;
var playerss;
    function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        videoId: 'r_pRpeEJCuw'
    }),
    players = new YT.Player('players', {
            videoId: 'QthPXicgrzg'
    });
    playerss = new YT.Player('playerss', {
        videoId: 'td9pyY-r0nE'
        });   
    }
    
    $(document).on('mouseover', '#player', function() {
      player.playVideo();
    });
    $(document).on('mouseout', '#player', function() {
      player.pauseVideo();
    });

    $(document).on('mouseover', '#players', function() {
      players.playVideo();
    });
    $(document).on('mouseout', '#players', function() {
      players.pauseVideo();
    });

    $(document).on('mouseover', '#playerss', function() {
      playerss.playVideo();
    });
    $(document).on('mouseout', '#playerss', function() {
      playerss.pauseVideo();
    });

    $(document).ready(function () {
      $("#myModal").modal();
    });
