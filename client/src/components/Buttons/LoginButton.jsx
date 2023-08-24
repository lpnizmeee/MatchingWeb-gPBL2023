import { useState } from "react";
import Signin from "../Account/Signin";
import { Link } from "react-router-dom";
const LoginButton = ({ userData, setUserData }) => {
  const [overlay, setOverlay] = useState(false);
  return (
    <div>
      {!userData ? (
        <button
          className="bg-red-400 py-2 px-5 w-32 rounded-3xl text-white hover:bg-red-500"
          onClick={(e) => {
            e.preventDefault();
            setOverlay(true);
          }}
        >
          Login
        </button>
      ) : (
        <button>
          <Link
            to="/user"
            className="text-primary bg-red-400 rounded-full p-2 hover:bg-red-500 font-semibold"
          >
            {userData.name}
          </Link>
        </button>
      )}
      {overlay && <Signin setOverlay={setOverlay} setUserData={setUserData} />}
    </div>
  );
};

export default LoginButton;
