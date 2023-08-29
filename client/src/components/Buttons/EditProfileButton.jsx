import React from "react";

const EditProfileButton = ({ text, onClick }) => {
  return (
    <button
      className="bg-green-400 hover:bg-green-500 py-3 px-10 w-fit rounded-3xl text-white"
      onClick={onClick}
    >
      {text}
    </button>
  );
};

export default EditProfileButton;
