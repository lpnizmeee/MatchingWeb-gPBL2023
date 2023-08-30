import { useState, useEffect } from "react";
// import menuData from "../constants/menuData.json";
import { InputField } from "./InputFields/InputField";
import GenericButton from "./Buttons/GenericButton";
import { motion, AnimatePresence } from "framer-motion";
import { loadUserData, storeUserData } from "../storage-managers/userData";
import axios from "axios";
const backendUrl = import.meta.env.VITE_REACT_BACKEND_URL || ""; //from .env files


const FilterButton = ({ text, selected, setSelected }) => {
  const filterStyle =
    selected === text
      ? "rounded-3xl py-2 px-6 bg-red-400 text-white w-fit"
      : "bg-transparent  rounded-3xl py-2 px-6 hover:bg-primary hover:text-white w-fit";
  return (
    <button className={filterStyle} onClick={(e) => setSelected(text)}>
      {text}
    </button>
  );
};

function handleMatch({ action, targetUser, userA }) {
    const data = {
      "action": action,
      "usernameA": userA.username,
      "usernameB": targetUser.username,
    }
    // console.log(data);
    const res = axios.put(`${backendUrl}/roommate/match/`, data, {
      withCredentials: true,
    });
    console.log(res.data);
    // window.location.reload();
};

const HandleStatus = ({status, targetUser, userA, reloadData}) => {
  switch (status) {
    case 0:
      return (
        <div className="flex flex-row gap-1">
          <button
            className="rounded-full bg-green-400 hover:bg-green-500 w-20 h-20 border-2 border-white"
            onClick={(e) => {
              handleMatch({ action: 1, targetUser: targetUser, userA: userA });
              reloadData(true);
            }}
          >
            Accept
          </button>

          <button
            className="rounded-full bg-gray-400 hover:bg-gray-500 w-20 h-20 border-2 border-white" 
            onClick={(e) => {
              handleMatch({ action: 0, targetUser: targetUser, userA: userA });
              reloadData(true);
            }}
          >
            Reject
          </button>
        </div>
      );

    case 1:
      return (
        <div>
          <div>Matched</div>
          <button
            className="rounded-full bg-red-400 hover:bg-red-500 w-20 h-20 border-2 border-white"
            onClick={(e) => {
              handleMatch({ action: 2, targetUser: targetUser, userA: userA });
              reloadData(true);
            }}
          >
            Cancel
          </button>
        </div>
      );

    case 2:
      return (
        <div>
          <button
            className="rounded-full bg-blue-400 hover:bg-blue-500 w-20 h-20 border-2 border-white"
            onClick={(e) => {
              handleMatch({ action: 3, targetUser: targetUser, userA: userA });
              reloadData(true);
            }}
          >
            Match now
          </button>
        </div>
      );

    case 3:
      return (
        <div className="flex flex-row gap-1">
          <button
            className="rounded-full bg-orange-400 hover:bg-orange-500 w-20 h-20 border-2 border-white"
            onClick={(e) => {
              handleMatch({ action: 4, targetUser: targetUser, userA: userA });
              reloadData(true);
            }}
          >
            Waiting
          </button>

          <button
            className="rounded-full bg-red-400 hover:bg-red-500 w-20 h-20 border-2 border-white" 
            onClick={(e) => {
              handleMatch({ action: 5, targetUser: targetUser, userA: userA });
              reloadData(true);
            }}
          >
            Cancel
          </button>
        </div>
      );

    default:
      return null;
  }
}


const MenuItem = ({ itemKey, item, addToCart, userA, reloadData }) => {
  // console.log(item);
  return (
    <motion.div
      key={itemKey}
      initial={{ opacity: 0, x: -100 }}
      animate={{ opacity: 1, x: 0 }}
      // exit={{ opacity: 0, x: 100 }}
      className="flex flex-col gap-5 bg-primary-light text-white  rounded-2xl h-full w-96 "
    >
      {/* <div className="rounded-bl-3xl rounded-t-xl bg-slate-200 flex flex-col items-center py-10">
        <img
          src={item.imageURL}
          alt={item.name}
          className="h-40 w-40 rounded-full"
        />
      </div> */}

      <div className="px-10 pb-5 pt-10 flex flex-col justify-between h-full">
        <div className="rounded-bl-3xl rounded-t-xl bg-white py-10">
          <div className="pl-10">
            <div className="flex flex-row flex-wrap">
              <div className="text-2xl font-body text-red-600 w-2/5">Name: </div>
              <div className="text-2xl flex flex-wrap font-body text-red-600 w-3/5">{item.name}</div>
            </div>
            <div className="flex flex-row">
              <div className="text-l text-stone-700 pt-2 w-2/5">Gender: </div> 
              <div className="text-l text-stone-700 pt-2 w-2/5">{item.gender ? "male" : "female"}</div>
            </div>
            <div className="flex flex-row">
              <div className="text-l text-stone-700 w-2/5">Age: </div> 
              <div className="text-l text-stone-700 w-2/5">{item.age}</div>
            </div>
            <div className="flex flex-row">
              <div className="text-l text-stone-700 w-2/5">Phone: </div> 
              <div className="text-l text-stone-700 w-2/5">{item.phoneNumber}</div>
            </div>
            <div className="flex flex-row">
              <div className="text-l text-stone-700 w-2/5">Longitude: </div> 
              <div className="text-l text-stone-700 w-2/5">{item.longtitude}</div>
            </div>
            <div className="flex flex-row">
              <div className="text-l text-stone-700 w-2/5">Latitude: </div> 
              <div className="text-l text-stone-700 w-2/5">{item.latitude}</div>
            </div>
          </div> 
        </div>
        <div className="justify-between items-center flex flex-row pt-5">
          <div className="text-xl font-body">Rent: {item.rent}$</div>
          <HandleStatus status={item.status} targetUser={item} userA={userA} reloadData={reloadData}/>
        </div>
      </div>
    </motion.div>
  );
};

//Get distinct categories from menuData
// let categoryList = [...new Set(menuData.map((item) => item.category))];
const Menu = ({ addToCart }) => {
  // const [selectedFilter, setSelectedFilter] = useState("All");
  const [query, setQuery] = useState("");
  const [data, setData] = useState([]);
  const [categoryList, setCategoryList] = useState([]);
  const [reload, setReload] = useState(false);
  const user = loadUserData();


  useEffect(() => {
    const fetchData = async () => {
      const data = { data: " " };
      const username = { "username": user.username };
      // console.log(username);
      // console.log(user);
      const res = await axios.post(`${backendUrl}/roommate/recommend/`, username, {
        withCredentials: true,
      });
      setData(res.data);
      // console.log(res.data);
      setReload(false);
    };
    fetchData();
  }, [reload]);


  // useEffect(() => {
  //   setCategoryList([...new Set(data.map((item) => item.category[0]))]);
  // }, [data]);


  const HandleSearch = async (e) => {
    e.preventDefault();
    if (query === "") return;
    if (query === "all") setQuery(" ");
    //TODO: Handle query
    const data = { "username": user.username,
                    "keyword": query};
    const res = await axios.post(`${backendUrl}/roommate/usersearch/`, data, {
      withCredentials: true,
    });
    setData(res.data);
    // setReload(true)
    // setSelectedFilter("All");
  };


  return (
    <div className="bg-white text-primary flex flex-col items-center gap-5 p-10 pt-32">
      <div className="text-4xl font-body">Roommate Recommend</div>
      <div className="w-1/2 flex flex-col lg:flex-row  gap-3 items-center">
        <InputField value={query} setValue={setQuery} placeholder="Search..." />
        <GenericButton text="Search" onClick={HandleSearch} />
      </div>
      {/* <div className="flex flex-row flex-wrap gap-3">
        <FilterButton
          text="All"
          selected={selectedFilter}
          setSelected={setSelectedFilter}
        />
        {categoryList.map((category, index) => (
          <FilterButton
            text={category}
            key={index}
            selected={selectedFilter}
            setSelected={setSelectedFilter}
          />
        ))}
      </div> */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-2 items-center mx-auto h-fit">
        <AnimatePresence>
          {data.map((item, index) =>
            // item.category[0] === selectedFilter || selectedFilter === "All" ? (
              <MenuItem
                key={index}
                itemKey={index}
                item={item}
                addToCart={addToCart}
                userA={user}
                reloadData={setReload}
              />
            // ) : null
          )}
        </AnimatePresence>
      </div>
    </div>
  );
};

export default Menu;
