// // /* ------------------SEND WHATSAPP MESSAGE----------------*/
// // function send_handle(item, valor, imgURL) {

// // var texto = `*Nova Solicitação:*

// // Olá, gostaria de comprar o produto abaixo:
        
// // *${item}*
// // *${valor}*


// // *Link do Produto:*
// // ${imgURL}
// // `;

        

// // var encodedTexto = encodeURI(texto);

// // var win = window.open(`https://wa.me/554733265159?text=${encodedTexto}`, '_blank');
// // }
// // /* ------------------SEND WHATSAPP MESSAGE----------------*/


// document.getElementById('searchForm').addEventListener('submit', function(event) {
//     var searchInput = document.querySelector('input[name="search"]');
    
//     // Se o campo de busca estiver vazio, personaliza a mensagem
//     if (!searchInput.value.trim()) {
//         searchInput.setCustomValidity('Por favor, insira algo no campo de busca.');
//         searchInput.reportValidity();
//         event.preventDefault();  // Impede o envio do formulário
//     } else {
//         searchInput.setCustomValidity('');  // Reseta a mensagem se estiver preenchido
//     }
// })