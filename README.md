<!-- PROJECT LOGO -->
  <h1 align="center">Hiding-images-using-steganography-techniques-with-compression-algorithms</h1>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#source-research">Source Research</a>
    </li>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


## Source Research 
[Source Article](https://www.researchgate.net/publication/333538111_Hiding_data_in_images_using_steganography_techniques_with_compression_algorithms)

The main development that the article deals with is a research on hiding images inside images using LSB Steganography encryption.<br/>
The researchers explain the neccesary background, and the results of the research.
3 main algorithms are used through out the research:
  1. Compressing the stego image using a DCT algorithm.
  2. Encrypting the stego image.
  3. Decoding the stego image into a cover image. using a LSB algorithms.

There are 2 overall methods that are being described in the article:
  1. Encoding the stego image into the cover image.
  2. Decoding the stego image from the cover image.

Our project is the implementation based on the described atricle.
  
  
<!-- ABOUT THE PROJECT -->
## About The Project

1. Encode -
   <ul>
    <li> DCT compress the stego image</li>
    <li> AES encrypt the stego image </li>
    <li> LSB encode the stego image inside the cover image </li>
  </ul>
  
2. Decode -
 <ul>
  <li> LSB decode the stego image from the cover image </li>
  <li> AES decrypt the stego image</li>
</ul>



### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/liorelisberg/Hiding-images-using-steganography-techniques-with-compression-algorithms
   ```
3. Install NPM packages
   ```sh
   npm install PIL, Crypto, pickle, scipy, skimage, base64, numpy
   ```


<!-- USAGE EXAMPLES -->
## Usage

![image](https://user-images.githubusercontent.com/14842875/122655977-7af66b00-d15f-11eb-8b03-fb080bc38bb4.png)
![image](https://user-images.githubusercontent.com/14842875/122655979-7e89f200-d15f-11eb-9e0a-d3bc184a391d.png)
![image](https://user-images.githubusercontent.com/14842875/122655987-88135a00-d15f-11eb-842f-ee7fa81dd656.png)


_For more examples, please refer to the [Documentation](https://example.com)_


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Lior Elisberg - LiorElisberg@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)

