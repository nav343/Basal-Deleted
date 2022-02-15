import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="text-gray-400 bg-gray-900 body-font">
      <div className="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a className="flex title-font font-medium items-center text-white mb-4 md:mb-0">
          <img
            src="https://cdn.discordapp.com/icons/941574043847508009/7a2c4253e7f6fcc6797f002088ec5a30.webp?size=128"
            alt="Logo"
            className="w-14 h-14 mr-2"
            ref={React.createRef()}
            draggable="false"
          />
          <span className="ml-3 text-xl">Basal</span>
        </a>
        <nav className="md:ml-auto flex flex-wrap items-center text-base justify-center">
          <Link
            to="/"
            className="mr-5 text-white hover:text-gray-300 cursor-pointer"
          >
            Home
          </Link>
          <Link
            to="/download"
            className="mr-5 text-white hover:text-gray-300 cursor-pointer"
          >
            Download
          </Link>
          <Link
            to="/docs"
            className="mr-5 text-white hover:text-gray-300 cursor-pointer"
          >
            Documentation
          </Link>
          <a
            href="https://github.com/SnmLogic/Basal/"
            target="_blank"
            className="mr-5 text-white hover:text-gray-300 cursor-pointer"
          >
            Github
          </a>
        </nav>
      </div>
    </header>
  );
}
