$(function(){

  var quotes =["“Bats frighten me.Its time my enemies share my dread","Im whatever Gotham needs me to be","I won’t kill you, but I don’t I have to save you.","We may fall but more will rise."];
  var favorite = quotes[Math.floor(Math.random() * quotes.length)]; 


   $(".destroy").on("click",function(){
   	var params =$(this).data('source');
   	var checkstr =  confirm(favorite);
   	if (checkstr == true) {
   		$.ajax({
   			type: 'post',
   			url: '/destroy/'+params,
   			success: function (dataCheck) {
   				location.reload();
   			}
   		});
   	}
   });
});