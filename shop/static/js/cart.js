
$(document).ready(function () {
  loadCartItems()


})



function loadCartItems() {
  var cartProcucts = sessionStorage.getItem("cartData");
  if (cartProcucts) {
    cartProcucts = JSON.parse(cartProcucts)

  } else {
    cartProcucts = []
  }

  $('.counter-ele').text(cartProcucts.length)
  var htmlStr = ''
  var totalPrice = 0;
  cartProcucts.map((obj => {
    totalPrice += parseInt(obj.price)
    htmlStr += `
        <li class="list-group-item d-flex justify-content-between lh-condensed">
              <div>
                <h6 class="my-0">${truncateString(obj.name, 25)}</h6>
                <small class="text-muted">category : ${obj.category}</small>
              </div>
              <span class="text-muted">₹ ${parseInt(obj.price).toLocaleString('en-IN')}</span>
            </li>
        `
  }))

  htmlStr += `
    <li class="list-group-item d-flex justify-content-between">
              <span>Total (INR)</span>
              <strong>₹ ${totalPrice.toLocaleString('en-IN')}</strong>
            </li>
    `

  $("#cart-items").html(htmlStr)
}

function continueToOrder() {
  var cartProcucts = sessionStorage.getItem("cartData");
  if (cartProcucts) {
    cartProcucts = JSON.parse(cartProcucts)

  } else {
    cartProcucts = []
  }
  if (cartProcucts.length < 1) {
    notif({
      msg: "Your cart is empty!, please add some products to continue",
      type: "error",
      opacity: 0.8,
      multiline: true
    })
  } else {



    $('#order-form').addClass('was-validated');
    $('#order-form').off('submit').submit(function (e) {

      var customer = getCustomer()
      var cartProcucts = sessionStorage.getItem("cartData");
      if (cartProcucts) {
        cartProcucts = JSON.parse(cartProcucts)

      } else {
        cartProcucts = []
      }
      if (!customer) {
        notif({
          msg: "Please Login/Regiser before payment!",
          type: "error",
          opacity: 0.8,
          multiline: true
        })
        userInfo()
      } else {
        var payload = {
          customer: customer,

          first_name: $("#firstName").val(),
          last_name: $("#lastName").val(),
          email: $("#email").val(),
          phone: $("#phone").val(),
          country: $("#country").val(),
          state: $("#state").val(),
          zip: $("#zip").val(),
          address1: $("#address").val(),
          address2: $("#address-2").val(),

          products: cartProcucts
        }

        $.ajax({
          url: baseUrl + 'order',
          data: JSON.stringify(payload),
          type: 'POST',
          contentType: "application/json",
          dataType: 'json',
          success: function (result) {

            if (result.status) {
              location.href = result.data.paymentUrl
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
            notif({
              msg: "A System error occured, Please try again!",
              type: "error",
              opacity: 0.8,
              multiline: true
            });
          }
        });

      }

      e.preventDefault();
    })
  }
}






