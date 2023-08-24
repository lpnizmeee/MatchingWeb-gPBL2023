import React from "react";
import { Link } from "react-router-dom";

const LogoTitle = ({ setActive }) => {
  return (
    <Link
      to="/"
      className="flex items-center gap-2"
      onClick={() => {
        setActive("");
        window.scrollTo(0, 0);
      }}
    >
      <img
        src={"/hanamilogo.png"}
        alt="logo"
        className="object-contain w-10 h-10"
        onDragStart={(e) => {
          e.preventDefault();
        }}
      />
      <p className="text-red-600 text-[25px] font-bold cursor-pointer flex md:flex-row flex-col font-body">
        Hanami &nbsp;
        <span className="hidden sm:block font-body text-[27px]">
          {" "}
          | CozyAbode
        </span>
      </p>
    </Link>
  );
};

export default LogoTitle;
