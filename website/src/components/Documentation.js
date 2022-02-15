import React from "react";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { okaidia } from "react-syntax-highlighter/dist/esm/styles/prism";

export default function Documentation() {
  return (
    <section className="flex bg-gray-800 text-white">
      <div className="sidebar bg-gray-900 w-3/4 h-full pl-5 pr-9 text-white pt-5">
        <div className="getting-started">
          <h1 className="text-2xl font-bold cursor-default">The Basal Book</h1>
          <h2 className="mt-5 font-semibold text-xl cursor-default">
            1. Getting Started
          </h2>
          <div className="flex flex-col mt-2">
            <a href="#installation">&emsp; Installation.</a>
            <a href="#hello_world">&emsp; Hello World.</a>
          </div>

          <h2 className="mt-5 font-semibold text-xl cursor-default">
            2. Variables
          </h2>
          <div className="flex flex-col mt-2">
            <a href="#define_variable">&emsp; Define a variable</a>
            <a href="#let_keyword">&emsp; Let Keyword.</a>
            <a href="#access_variable">&emsp; Accessing the variable.</a>
            <a href="#variable_scope">&emsp; Variable scope.</a>
          </div>

          <h2 className="mt-5 font-semibold text-xl cursor-default">
            3. Loops
          </h2>
          <div className="flex flex-col mt-2">
            <a href="#for_loop">&emsp; For Loop.</a>
            <a href="#while_loop">&emsp; While Loop.</a>
          </div>

          <h2 className="mt-5 font-semibold text-xl cursor-default">
            4. Functions
          </h2>
          <div className="flex flex-col mt-2">
            <a href="#functions">&emsp; What is a function.</a>
            <a href="#func_keyword">&emsp; Func keyword.</a>
            <a href="#">&emsp; Creating a function.</a>
            <a href="#">&emsp; Adding Parameters.</a>
            <a href="#accessing_functions">&emsp; Accessing the function.</a>
          </div>

          <h2 className="mt-5 font-semibold text-xl cursor-default">
            5. About
          </h2>
          <div className="flex flex-col mt-2">
            <a href="#basal">&emsp; Basal.</a>
            <a href="#devs">&emsp; The Developers.</a>
          </div>
          <hr className="mt-10 pb-10" />
        </div>
      </div>

      <div className="ml-10">
        <h1 className="font-bold text-4xl mt-5 font-poppins">The Basal Book</h1>
        <h2 className="mt-5 font-semibold text-2xl"> Getting Started</h2>
        <h3 className="mt-5 font-semibold text-xl">&emsp; Installation</h3>
        <div className="ml-7 mt-2 w-fit" id="installation">
          <p className="pr-20">
            Visit the downloads page and click on the Download button. Once the
            installation is complete, search for ENV in your windows searchbar,
            open it and click on 'path', click on 'new' and add the path where
            you can installed the basalc.exe file. and click save. Then open
            your teminal and type 'basalc --help', if you see a help desk then
            you are good to go.
          </p>
          <img
            src="https://cdn.discordapp.com/attachments/926017485302534144/942741424837914704/unknown.png"
            alt="Download Page image."
            className="mt-5 h-60"
          />
        </div>

        <h3 className="mt-10 font-semibold text-xl" id="hello_world">
          &emsp; Hello World
        </h3>
        <p className="ml-6 pr-20 mt-5">
          Writing hello world in Basal is really simple. Use 'out' keyword with
          a "Hello World" message in it to print Hello World into the console.
        </p>
        <SyntaxHighlighter
          language="javascript"
          style={okaidia}
          customStyle={{ width: "fit-content", marginLeft: "20px" }}
        >
          {hello_world_code}
        </SyntaxHighlighter>

        <h2 className="mt-10 font-semibold text-2xl"> Variables</h2>
        <h3 className="mt-5 font-semibold text-xl" id="define_variable">
          &emsp; Define a Variable
        </h3>
        <p className="ml-6 mt-2">
          Use the 'let' keyword followed by the name of the variable for
          defining it. Here is an example.
        </p>
        <SyntaxHighlighter
          language="javascript"
          style={okaidia}
          customStyle={{ width: "fit-content", marginLeft: "20px" }}
        >
          {variable_code}
        </SyntaxHighlighter>

        <h3 className="mt-5 font-semibold text-xl" id="let_keyword">
          &emsp; Let keyword
        </h3>
        <p className="ml-6 mt-2 pr-20">
          Let is an in-built keyword that is used for labelling variables. For
          defining a variable, use the 'let' keyword followed by the name of the
          variable.
        </p>
        <SyntaxHighlighter
          language="javascript"
          style={okaidia}
          customStyle={{ width: "fit-content", marginLeft: "20px" }}
        >
          {variable_code_v2}
        </SyntaxHighlighter>

        <h3 className="mt-5 font-semibold text-xl" id="access_variable">
          &emsp; Accessing the variable
        </h3>
        <p className="ml-6 mt-2 pr-20">
          For accessing a variable just type out its name. Here is an example.
        </p>
        <SyntaxHighlighter
          language="javascript"
          style={okaidia}
          customStyle={{ width: "fit-content", marginLeft: "20px" }}
        >
          {access_variable}
        </SyntaxHighlighter>

        <h3 className="mt-5 font-semibold text-xl" id="variable_scope">
          &emsp; Variable Scope
        </h3>
        <p className="ml-6 mt-2 pr-20">Coming soon...........</p>

        <h2 className="mt-10 font-semibold text-2xl"> Loops</h2>
        <h3 className="mt-5 font-semibold text-xl" id="for_loop">
          &emsp; For Loop
        </h3>
        <p className="ml-6 mt-2 pr-20">
          Like all other normal languages, basal also uses the for keyword for
          'for loops'. Here is a ranging example, this code will go from 20 to
          100 and will add 10 to it.
        </p>
        <SyntaxHighlighter
          language="javascript"
          style={okaidia}
          customStyle={{ width: "fit-content", marginLeft: "20px" }}
        >
          {for_loop}
        </SyntaxHighlighter>

        <h3 className="mt-5 font-semibold text-xl" id="while_loop">
          &emsp; While Loop
        </h3>
        <p className="ml-6 mt-2 pr-20">
          As usual While loops are loops which will not stop until a certain
          statement is false. While Loop can be used by using the while keyword.
          Here is an example, this loop will never stop as the value of 1 is
          always 1. You can also use true instead of 1.
        </p>
        <SyntaxHighlighter
          language="javascript"
          style={okaidia}
          customStyle={{ width: "fit-content", marginLeft: "20px" }}
        >
          {while_loop}
        </SyntaxHighlighter>

        <h2 className="mt-10 font-semibold text-2xl"> Functions</h2>
        <h3 className="mt-5 font-semibold text-xl" id="functions">
          &emsp; What is a Function
        </h3>
        <p className="ml-6 mt-2 pr-20">
          Functions is a block of related statements designed to perform a
          computational, logical, or evaluative task. The idea is to put some
          commonly or repeatedly done tasks together and make a function so that
          instead of writing the same code again and again for different inputs,
          we can do the function calls to reuse code contained in it over and
          over again. Functions can be both built-in or user-defined. It helps
          the program to be concise, non-repetitive, and organized.
        </p>

        <h3 className="mt-5 font-semibold text-xl" id="func_keyword">
          Func Keyword
        </h3>
        <p className="ml-6 mt-2 pr-20">
          In Basal functions are defined using the func keyword followed by the
          name of the function. A function can have parameters or arguments.
          Here is an example of a function that takes 2 parameters (for this
          example I am using i32 value or int or numbers) and adds those two
          numbers.
        </p>
        <SyntaxHighlighter
          language="javascript"
          style={okaidia}
          customStyle={{ width: "fit-content", marginLeft: "20px" }}
        >
          {function_example}
        </SyntaxHighlighter>

        <h3 className="mt-5 font-semibold text-xl" id="accessing_functions">
          Accessing the function.
        </h3>
        <p className="ml-6 mt-2 pr-20">
          For accessing function, you have to call out by its name and pass in
          the parameters if any. Pass (any) parameters inside paranthesis.
        </p>
        <SyntaxHighlighter
          language="javascript"
          style={okaidia}
          customStyle={{ width: "fit-content", marginLeft: "20px" }}
        >
          {access_function}
        </SyntaxHighlighter>

        <h2 className="mt-10 font-semibold text-2xl"> About</h2>
        <h3 className="mt-5 font-semibold text-xl" id="basal">
          &emsp; Basal
        </h3>
        <p className="ml-6 mt-2 pr-20">
          Basal is a general purpose low level compiled programming language
          that compiles its code to C, Basal is made using Python v3.10.0.
          Development of Basal was started at 11 February 2022 by Snm Logic,
          Bunch-Of-Cells and Mochii.
        </p>

        <h3 className="mt-5 font-semibold text-xl" id="devs">
          &emsp; The Developers
        </h3>
        <p className="ml-6 mt-2 pr-20 mb-10">
          The core developers of Basal are Snm Logic, Bunch-Of-Cells and Mochii.
          The Lexer and the Parser was written by Bunch-of-cells, Writing and
          testing the compiler was done by Mochii. The docs (this page xD) and
          the website was made by Snm Logic (btw I am the repo owner).
        </p>
      </div>
    </section>
  );
}

// Code Example
const hello_world_code = `out("Hello World")`;
const variable_code = `let name = "John"`;
const variable_code_v2 = `let {name} = {value}`;
const access_variable = `out(var_name)`;
const for_loop = `for i in (20..101) {
  out(i)
  out(i + 10)
}`;
const while_loop = `while 1 {
  out("I am stuck inside a loop, Plz save me !!!.")
}`;
const function_example = `func add(a, b) {
  return a + b
}`;
const access_function = `func add(a, b) {
  return a + b
}

add(10, 20)`;
