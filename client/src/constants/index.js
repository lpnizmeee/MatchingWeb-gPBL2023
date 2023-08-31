import { cuong, hnam, pnam, anon, thanh, hadinh } from "../assets";

const members = [
  {
    name: "Le Phuong Nam",
    image: pnam,
    role: "Fullstack Developer",
    description:
      "Sophomore student at Hanoi University of Science and Technology, majoring in Computer Science",
  },
  {
    name: "Hoang Gia Anh",
    image: cuong,
    role: "Fullstack Developer",
    description:
      "Sophomore student at Hanoi University of Science and Technology, majoring in Computer Science",
  },
  {
    name: "HARA Rikuto",
    image: pnam,
    role: "Leader",
    description:
      "Junior student at Shibaura Institute of Technology, majoring in Information Engineering",
  },
  {
    name: "Do Thuy Duong",
    image: hnam,
    role: "Back-end Developer",
    description:
      "Sophomore student at Hanoi University of Science and Technology, majoring in Computer Science",
  },
];

export const navLinks = [
  {
    id: "home",
    title: "HOME",
    pathname: "/",
  },
  {
    id: "menu",
    title: "FINDROOMATE",
    pathname: "/menu",
  },
  {
    id: "about",
    title: "ABOUT",
    pathname: "/about",
  },
  {
    id: "map",
    title: "MAP",
    pathname: "/map",
  },
];

export const adminNavLinks = [
  {
    id: "admin",
    title: "ADMIN",
    pathname: "/admin",
  },
];

export { members };
