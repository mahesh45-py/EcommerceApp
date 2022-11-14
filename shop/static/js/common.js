
var baseUrl = "http://localhost:8000/"

$(document).ready(function(){
    
  
    showCartsCountWidget()
    checkSession()
})

function truncateString(str, num) {
  if (str.length > num) {
    return str.slice(0, num) + "...";
  } else {
    return str;
  }
}

/**********************************************
*       Customer Session Related Functions Starting
*********************************************/
function addCustomerSession(res) {
  sessionStorage.setItem('customer', JSON.stringify(res))
}
function clearCustomerSession() {
  sessionStorage.removeItem('customer')
  checkSession()
}
function getCustomer(){

  var data = JSON.parse(sessionStorage.getItem('customer'))
  return data ? data : ''
}

function checkSession(){
  var customer = getCustomer()
  if(customer){
    $(".userName").text(customer.first_name+' '+customer.last_name)
    $(".newUser").hide()
    $(".existingUser").show()
  }else{
    $(".newUser").show()
    $(".existingUser").hide()
  }
}

function logout(){
  if(confirm("are you sure to logout")){
    clearCustomerSession()
    notif({
      msg: "Logout Successful",
      type: "success",
      opacity:0.8,
      multiline: true
    }) 
  }
}

function myorders(){
  alert("this option will be added soon.......")
}

function userInfo(){
  $("#register-form").trigger("reset");
  $("#login-form").trigger("reset");
  $("#userInfo").modal("show")
}



function invokeRegister(){
  $('#register-form').addClass('was-validated');
  $('#register-form').off('submit').submit(function (e) {
    if($("#reg-password").val() != $("#reg-confirmpassword").val()){
      notif({
        msg: "Password and Confirm Password should be same",
        type: "warning"
      });
      e.preventDefault();
      return
    }
      var payload = {
        'first_name': $("#reg-firstName").val(),
        'last_name': $("#reg-lastName").val(),
        'email': $("#reg-email").val(),
        'phone': $("#reg-phone").val(),
        'password': $("#reg-password").val()
      }
      $.ajax({
        url: baseUrl + 'customer',
        data: JSON.stringify(payload),
        type: 'POST',
        contentType: "application/json",
        dataType: 'json',
        success: function(result) {
            notif({
              msg:result.message,
              type:  result.status ? "success" : "error",
              opacity:0.8,
              multiline: true
            })
            if(result.status){
              
              $(".login-tab a").trigger("click")
              $("#login-email").val($("#reg-email").val())
              $("#register-form").trigger("reset");
            }
        },
        error: function(){
          notif({
            msg: "A System error occured, Please try again!",
            type: "error",
            opacity:0.8,
            multiline: true
          });
        }
    });
      e.preventDefault();
      
  })
}

function invokeLogin(){
  $('#login-form').addClass('was-validated');
  $('#login-form').off('submit').submit(function (e) {
      var payload = {
        'email': $("#login-email").val(),
        'password': $("#login-passsword").val()
      }
      $.ajax({
        url: baseUrl + 'customer',
        data: JSON.stringify(payload),
        type: 'PUT',
        contentType: "application/json",
        dataType: 'json',
        success: function(result) {
          notif({
            msg:result.message,
            type:  result.status ? "success" : "error",
            opacity:0.8,
            multiline: true
          }) 
          if(result.status){
            $("#userInfo").modal("hide")
            addCustomerSession(result.data)
            checkSession()
          }
          
        },
        error: function(){
          notif({
            msg: "a System Error Occured! please try again",
            type:  "error",
            opacity:0.8,
            multiline: true
          }) 
          
        }
    });
      e.preventDefault();
      
  })
}




/**********************************************
*       Customer Session Related Functions Ending
*********************************************/



function showCartsCountWidget() {


    var cartProcucts = sessionStorage.getItem("cartData");
    if(cartProcucts) {
      cartProcucts = JSON.parse(cartProcucts)
    } else {
      cartProcucts = []
    }

    $('.cart-count').text(cartProcucts.length)
  }
