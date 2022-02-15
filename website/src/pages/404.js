import React from "react";
import { Link } from "react-router-dom";

export default function _404() {
  return <Main />;
}

const Main = () => {
  document.title = "404 Page Not Found";
  return (
    <section className="h-screen grid place-items-center text-center bg-gray-800 w-screen ">
      <div className="w-screen">
        <h1 className="text-indigo-500 font-bold text-5xl">Oops !!!</h1>
        <h3 className="text-white text-xl mt-5 mb-10">
          The page you are looking for was not found.
        </h3>
        <Link
          to="/"
          className="bg-indigo-500 p-5 rounded-full text-white font-semibold hover:bg-indigo-800"
        >
          Back To Home
        </Link>
      </div>
    </section>
  );
};
