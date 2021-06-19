var updateBtn = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        if (user === 'AnonymousUser') {
            console.log("Not log in")
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log("logg in")
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log("item is add")
        });
}



// var inputBtn = document.getElementsByClassName('quantity')
//
// for (var i = 0; i < inputBtn.length; i++) {
//     inputBtn[i].addEventListener('click', function () {
//         var productId = this.dataset.product
//         var quantity = this.value
//         console.log('productId:', productId, 'quantity:', quantity)
//         updateQuantity(productId, quantity)
//     })
//
// }
//
// function updateQuantity(productId, quantity) {
//     var url = '/update_cart/'
//
//     fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken,
//         },
//         body: JSON.stringify({'productId': productId, 'quantity': quantity})
//     })
//         .then((response) => {
//             return response.json()
//         })
//         .then((data) => {
//             console.log("item is update")
//         })
// }
//
//
