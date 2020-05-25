$(function() {
  $("#cpaste").click(function() {
  $(this).focus();
  $(this).select();
  document.execCommand('cpaste');
  $(this).after("Copied to clipboard");
  });
 });
