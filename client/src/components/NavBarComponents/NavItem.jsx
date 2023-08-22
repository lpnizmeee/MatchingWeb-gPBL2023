import React from "react";
import { Link } from "react-router-dom";
const NavItem = ({ nav, active, setActive }) => {
  return (
    <li
      key={nav.id}
      className={`${
        active === nav.title ? "text-red-600" : "text-red-600"
      } hover:text-red-600 text-[18px] font-medium cursor-pointer`}
      onClick={() => {
        setActive(nav.title);
      }}
    >
      <Link to={`${nav.pathname}`}>{nav.title}</Link>
    </li>
  );
};

export default NavItem;
