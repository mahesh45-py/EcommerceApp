
$(document).ready(function(){
    checkProduct()
})


function checkProduct(){
    var cartProcucts = sessionStorage.getItem("cartData");
    if(cartProcucts) {
        cartProcucts = JSON.parse(cartProcucts)
        
    } else {
        cartProcucts = []
    }
    
    var productAvl = $.grep(cartProcucts, function (obj) {
        return (obj.id == product.id)
    });
    if (productAvl.length > 0) {
        $(".cartBtn").html(' <i class="fas fa-shopping-cart mr-1"></i> Remove From Cart').removeClass('btn-primary').addClass('btn-danger')
    }else{
        $(".cartBtn").html(' <i class="fas fa-shopping-cart mr-1"></i> Add To Cart').removeClass('btn-danger').addClass('btn-primary')
    }
}
function toggleProductToCart() {
    var ele = $(".cartBtn")
    var cartProcucts = sessionStorage.getItem("cartData");
    if (cartProcucts) {
        cartProcucts = JSON.parse(cartProcucts)
    } else {
        cartProcucts = []
      
    }
    if(parseInt(product.stock)<1){
      notif({
        msg: "This product is currently Out of stock, please try after sometime",
        type: "error",
        opacity: 0.8,
        multiline: true
      });
    }
    var productAvl = $.grep(cartProcucts, function (obj) {
      return (obj.id == product.id)
    });

    if (productAvl.length > 0) {

      cartProcucts = $.grep(cartProcucts, function (obj) {
        return !(obj.id == product.id)
      });

      ele.html(' <i class="fas fa-shopping-cart mr-1"></i> Add To Cart').removeClass('btn-danger').addClass('btn-primary')

    } else {

      cartProcucts.push({
        id: product.id,
        name: product.name,
        price: product.price,
        stock: product.stock,
        image: product.image,
        category:product.category
      })

      ele.html(' <i class="fas fa-shopping-cart mr-1"></i> Remove From Cart').removeClass('btn-primary').addClass('btn-danger')
    }

    sessionStorage.setItem("cartData", JSON.stringify(cartProcucts));

    showCartsCountWidget()
  }