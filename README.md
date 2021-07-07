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
    <li><a href="#improvments">Improvments</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


## Source Research 
[Source Article](https://www.researchgate.net/publication/333538111_Hiding_data_in_images_using_steganography_techniques_with_compression_algorithms)

The main development that the article deals with is a research on hiding images inside images using LSB Steganography encryption.<br/>
The researchers explain the neccesary background, and the results of the research.<br/><br/>
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
### The cover image:
![test200](https://user-images.githubusercontent.com/14842875/122656557-446f1f00-d164-11eb-8bb7-b828a0f6728d.jpg) <br/><br/>

### The stego image:
![secret](https://user-images.githubusercontent.com/14842875/122656568-5650c200-d164-11eb-8913-b3fb3378afcc.jpg) <br/><br/>

### Run "driver.py":
![image](https://user-images.githubusercontent.com/14842875/122655977-7af66b00-d15f-11eb-8b03-fb080bc38bb4.png) <br/><br/>

### For encoding -  press 1 + enter:
![image](https://user-images.githubusercontent.com/14842875/122655979-7e89f200-d15f-11eb-9e0a-d3bc184a391d.png) <br/><br/>

### For decoding -  press 2 + enter:
![image](https://user-images.githubusercontent.com/14842875/122655987-88135a00-d15f-11eb-842f-ee7fa81dd656.png) <br/><br/>


<!-- IMPROVMENTS -->
## Improvments
  The project contains 3 improvments (1 for each used algorithm):
  1. LSB - in the article, the researchers are discussing about injecting the data in the 8th bit of each block.<br/>
     For security improvments, we desided to inject the data in the 6&7th bit.<br/>
     From:<br/>
     ![image](https://user-images.githubusercontent.com/14842875/122656699-b85df700-d165-11eb-9e8c-b13ccd106dc7.png) <br/><br/>
     To:<br/>
     ![image](https://user-images.githubusercontent.com/14842875/122656702-c01d9b80-d165-11eb-8691-8a2ef3399f17.png) <br/><br/>

  2. DCT - in the article, the researchers mention that the described algorithm solely support .JPG image format.<br/>
     For diversity improvments, we desided to support few other formats.<br/>
     after some research, we found that the DCT can support (and improve) the outcome of the following formats  - {jpg, jfif, jp2, bmp}<br/><br/>
     ![image](https://user-images.githubusercontent.com/14842875/122656862-18a16880-d167-11eb-8649-81dec3484cb2.png)

  3. AES - in the article, there's no implemention or mentioning of any cryptographic algorithm that has been used in the article.
     The researchers talk about it abstractly.
     we decided to implement a modern & well documented crypto algorithm.
     After some research, we found out that there are few popular algorithms, such as: DES, RSA, BLOWFISH, AES. 
     Due to great documantation and online examples, as well as great results, we decided to implement the AES algorithms.

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
Mendel Amar - mendlamar11@gmail.com

Project Link: [https://github.com/liorelisberg/Hiding-images-using-steganography-techniques-with-compression-algorithms](https://github.com/liorelisberg/Hiding-images-using-steganography-techniques-with-compression-algorithms)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Source Article](https://www.researchgate.net/publication/333538111_Hiding_data_in_images_using_steganography_techniques_with_compression_algorithms)
* [DCT](https://en.wikipedia.org/wiki/Discrete_cosine_transform)
* [LSB Encryption](https://www.degruyter.com/document/doi/10.1515/nleng-2016-0010/html)
* [AES Encryption](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

