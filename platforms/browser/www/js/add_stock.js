function add_stock(){
  var stock_name = $("#stock_name_input").val();
  var buy_price = $("#buy_price").val();
  var buy_date = $("#buy_date").val();
  var action = $('#add_stock').attr('action');
  var method = $('#add_stock').prop('method');
  var buy_quantity = $("#buy_quantity").val();
  var submit_button = $('#submit_button');
  var details = {stock_name: stock_name, buy_price: buy_price, buy_date: buy_date, buy_quantity:buy_quantity};
  console.log(action);
  if((stock_name=='') || (buy_price=='') || (buy_date=='')){
    if(stock_name==''){
        ons.notification.toast('Enter Stock Name', { timeout: 2000, animation: 'fall'}); // Shows from 0s to 2s
        return false;
    }
    if(buy_price==''){
        ons.notification.toast('Enter Buy Price', { timeout: 2000, animation: 'fall'}); // Shows from 0s to 2s
        return false;
    }
    if(buy_date==''){
        ons.notification.toast('Enter Buy Date', { timeout: 2000, animation: 'fall'}); // Shows from 0s to 2s
        return false;
    }
  }
  else{
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8000/stocks/add/",
      data: details,
      beforeSend: function(){
        submit_button.prop("disabled",true);
        submit_button.val('Please Wait');
      },
      success: function(data){
        submit_button.prop("disabled",false);
        if(data=="success")
          {
            submit_button.prop("disabled",true);
            ons.notification.toast(data, { timeout: 2000, animation: 'fall'});
            var r = confirm("New Stock Added!");
             if (r == true){
               window.location.reload();
             }
          }
          else
          {
            submit_button.prop("disabled",false);
            //ons.notification.toast(data, { timeout: 2000, animation: 'fall'}); // Shows from 0s to 2s
            ons.notification.toast(data, { timeout: 2000, animation: 'fall'}); // Shows from 0s to 2s
            var r = confirm("New Stock Added!");
             if (r == true){
               window.location.reload();
             }
          }
        }
      });
     }
     return false;
  }
