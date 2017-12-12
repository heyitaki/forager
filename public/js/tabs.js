$(document).ready(function() {
  $('.tab').click(function() {
    $('.tabs-wrapper').find('button').removeClass('active');
    $(this).addClass('active');
    $(document).find('.tab-content').removeClass('active');
    $(`#${$(this).attr('name')}`).addClass('active');
  });
});