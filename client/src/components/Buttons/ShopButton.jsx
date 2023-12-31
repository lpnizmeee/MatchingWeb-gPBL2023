import { useState, useEffect } from "react";
import ShoppingCartIcon from "../../assets/ShoppingCartIcon";
import { Navigate, Link } from "react-router-dom";

const ShopButton = ({ itemCount }) => {
  return (
    <Link to="/cart">
      <button className="fixed bottom-0 right-0 z-30 text-primary bg-red-400 p-3 m-5 rounded-full hover:bg-red-500">
        <ShoppingCartIcon itemCount={itemCount} />
      </button>
    </Link>
  );
};

export default ShopButton;
