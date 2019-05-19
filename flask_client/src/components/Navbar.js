import React from "react";

class Navbar extends React.Component {
  render() {
    return (
      <div>
        <header class="header-area clearfix">
          {"<!-- Close Icon -->"}{" "}
          <div class="nav-close">
            <i class="fa fa-close" aria-hidden="true" />
          </div>
          {"<!-- Logo -->"}
          <div class="logo">
            <a href="index.html">
              <img src="img/core-img/logo.png" alt="" />
            </a>
          </div>
          {"<!-- Amado Nav -->"}
          <nav class="amado-nav">
            <ul>
              <li class="active">
                <a href="index.html">Home</a>
              </li>
              <li>
                <a href="shop.html">Shop</a>
              </li>
              <li>
                <a href="product-details.html">Product</a>
              </li>
              <li>
                <a href="cart.html">Cart</a>
              </li>
              <li>
                <a href="checkout.html">Checkout</a>
              </li>
            </ul>
          </nav>
          {"<!-- Button Group -->"}
          <div class="amado-btn-group mt-30 mb-100">
            <a href="#" class="btn amado-btn mb-15">
              %Discount%
            </a>
            <a href="#" class="btn amado-btn active">
              New this week
            </a>
          </div>
          {"<!-- Cart Menu -->"}
          <div class="cart-fav-search mb-100">
            <a href="cart.html" class="cart-nav">
              <img src="img/core-img/cart.png" alt="" /> Cart <span>(0)</span>
            </a>
            <a href="#" class="fav-nav">
              <img src="img/core-img/favorites.png" alt="" /> Favourite
            </a>
            <a href="#" class="search-nav">
              <img src="img/core-img/search.png" alt="" /> Search
            </a>
          </div>
          {"<!-- Social Button -->"}
          <div class="social-info d-flex justify-content-between">
            <a href="#">
              <i class="fa fa-pinterest" aria-hidden="true" />
            </a>
            <a href="#">
              <i class="fa fa-instagram" aria-hidden="true" />
            </a>
            <a href="#">
              <i class="fa fa-facebook" aria-hidden="true" />
            </a>
            <a href="#">
              <i class="fa fa-twitter" aria-hidden="true" />
            </a>
          </div>
        </header>
        {"<!-- Header Area End -->"}
      </div>
    );
  }
}

export default Navbar;