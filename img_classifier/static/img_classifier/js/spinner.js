$(document).ready( function() { 
  $('#spinner').addClass('hide');
  $('#upload-img').on('click', function()
  {
    $('#spinner').removeClass('hide');
  });
});