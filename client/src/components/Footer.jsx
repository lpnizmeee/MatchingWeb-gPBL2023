import React from "react";

const Footer = () => {
  return (
    <footer className="bg-red-500 text-center text-lg-start w-full">
      <div
        className="text-center p-3"
        style={{ backgroundColor: "rgba(0, 0, 0, 0.2)" }}
      >
        <a className="text-white" href="/">
          © 2023 Copyright Hanami Team
        </a>
      </div>
    </footer>
  );
};
export default Footer;
