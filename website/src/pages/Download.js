import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import DownloadMain from "../components/DownloadMain";

export default function Download() {
  document.title = "Basal - Download";
  return (
    <>
      <Header />
      <div className="bg-gray-900 pb-14">
        <DownloadMain />
      </div>
      <Footer />
    </>
  );
}
