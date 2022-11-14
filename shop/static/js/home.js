
$(document).ready(function () {
    checkPreviousPayment()
  
    
  })

function checkPreviousPayment() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const order_id = urlParams.get('order_id')
    if (order_id) {
      var payload = {
        order_id: order_id
      }
      $("body").css("cursor", "progress");
      $.ajax({
        url: baseUrl + 'order',
        data: JSON.stringify(payload),
        type: 'PUT',
        contentType: "application/json",
        dataType: 'json',
        success: function (result) {
            $("body").css("cursor", "default");
          if (result.status) {
            notif({
              msg: result.message,
              type: "success",
              opacity: 0.8,
              multiline: true
            });
            sessionStorage.removeItem('cartData')
            showCartsCountWidget()
            window.history.pushState({}, document.title, "/");
            
          } else {
            notif({
              msg: result.message,
              type: "error",
              opacity: 0.8,
              multiline: true
            });
          }
        },
        error: function () {
            $("body").css("cursor", "default");
          notif({
            msg: "A System error occured, Please try again!",
            type: "error",
            opacity: 0.8,
            multiline: true
          });
        }
      });
    }
  
  }