import { motion } from "framer-motion";
import { styles } from "../../styles";
import GenericButton from "../Buttons/GenericButton";
const Hero = () => {
  return (
    <div className={`relative w-full h-screen mx-0 `}>
      <div
        className={`absolute inset-0 top-[120px]  max-w-7xl mx-auto ${styles.paddingX} flex flex-row items-start gap-5`}
      >
        <div className="flex flex-col gap-5 w-3/5 pt-60">
          <div className="bg-pink-special p-10 rounded-3xl">
          <div className="text-5xl font-body text-red-600 pb-5">Roommate & Rental Matchmaker</div>
          <div className="text-red-500">
            Welcome to CozyAbode, your One-Stop Solution for Finding the Perfect House and Compatible Roommates.{" "}
          </div>
          </div>
          {/* <GenericButton text="Order Now" /> */}
        </div>
      </div>
    </div>
  );
};

export default Hero;
