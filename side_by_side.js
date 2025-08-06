let l11= ['./chaarAdhyay\\0\\350.nef', './chaarAdhyay\\0_0\\350.nef', './chaarAdhyay\\0_1\\350.nef', './chaarAdhyay\\10\\350.nef', './chaarAdhyay\\11\\350.nef', './chaarAdhyay\\12\\350.nef', './chaarAdhyay\\13\\350.nef', './chaarAdhyay\\14\\350.nef', './chaarAdhyay\\15\\350.nef', './chaarAdhyay\\17\\350.nef', './chaarAdhyay\\18\\350.nef', './chaarAdhyay\\19\\350.nef', './chaarAdhyay\\1\\350.nef', './chaarAdhyay\\2\\350.nef', './chaarAdhyay\\3\\350.nef', './chaarAdhyay\\4\\350.nef', './chaarAdhyay\\5\\350.nef', './chaarAdhyay\\7\\350.nef', './chaarAdhyay\\8\\350.nef', './chaarAdhyay\\9\\350.nef']
let l22= ['chessboard\\camShader0\\0.png', 'chessboard\\camShader0_0\\0_0.png', 'chessboard\\camShader0_1\\0_1.png', 'chessboard\\camShader10\\10.png', 'chessboard\\camShader11\\11.png', 'chessboard\\camShader12\\12.png', 'chessboard\\camShader13\\13.png', 'chessboard\\camShader14\\14.png', 'chessboard\\camShader15\\15.png', 'chessboard\\camShader17\\17.png', 'chessboard\\camShader18\\18.png', 'chessboard\\camShader19\\19.png', 'chessboard\\camShader1\\1.png', 'chessboard\\camShader2\\2.png', 'chessboard\\camShader3\\3.png', 'chessboard\\camShader4\\4.png', 'chessboard\\camShader5\\5.png', 'chessboard\\camShader7\\7.png', 'chessboard\\camShader8\\8.png', 'chessboard\\camShader9\\9.png']

let l1 = l11.map(item => item.replace("chaarAdhyay", "UndistortAndCropThese").replace("nef", "png"));
//let l1= l111.map(item => item.replace("nef", "png"));
let l2 = l22.map(item => item.replace("chessboard\\camShader", "UndistortAndCropThese\\"));

// Check if lengths match
if (l1.length !== l2.length) {
  console.warn("Warning: The two lists have different lengths.");
}

const container = document.getElementById("pairs");

// Render each pair
for (let i = 0; i < Math.min(l1.length, l2.length); i++) {
  const pairCol = document.createElement("div");
  pairCol.className = "pair";

  pairCol.innerHTML = `
    <div class="row">
      <div class="col-md-6 text-center">
        <img src="${l1[i]}" alt="Image ${i+1} - List 1" class="img-fluid">
        <p> Undistorted real-world image</p>
      </div>
      <div class="col-md-6 text-center">
        <img src="${l2[i]}" alt="Image ${i+1} - List 2" class="img-fluid">
        <p> Simulated image. Pose ${l1[i].substring(l1[i].indexOf("\\")+1, l1[i].lastIndexOf("\\"))}</p>
      </div>
    </div>
  `;

  container.appendChild(pairCol);
}