function solve() {
   const addBtns = Array.from(document.querySelectorAll('.add-product'));
   const output = document.querySelector('textarea');
   const checkoutBtn = document.querySelector('.checkout');
   addBtns.forEach(btn => btn.addEventListener('click', addProduct))
   checkoutBtn.addEventListener('click', buy);
   let order = {};

   function addProduct() {
      const product = Array.from(this.parentElement.parentElement.children);
      const productTitle = product[1].children[0].innerText;
      const productPrice = Number(product[3].innerText);
      if (!order.hasOwnProperty(productTitle)) {
         order[productTitle] = 0;
      }
      order[productTitle] += productPrice;
      output.textContent += `Added ${productTitle} for ${productPrice.toFixed(2)} to the cart.\n`;
   }

   function buy() {
      let products = [];
      let totalPrice = 0;
      Object.keys(order).forEach(product => {
         products.push(product);
         totalPrice += Number(order[product]);
      })
      output.textContent += `You bought ${products.join(', ')} for ${totalPrice.toFixed(2)}.`
      addBtns.forEach(btn => btn.disabled = true);
      checkoutBtn.disabled = true;
   }
}