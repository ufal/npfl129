- `--criterion=gini --max_depth=2 --seed=42`
```
Train acc: 94.1%
Test acc: 85.7%
```
<svg width="536pt" height="269pt" viewBox="0.0 0.0 536.0 269.0" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g class="graph" transform="scale(1 1) rotate(0) translate(4 265)">
<title>Tree</title>
<polygon fill="none" stroke="none" points="-4,4 -4,-265 532,-265 532,4 -4,4"/>
<g class="node"><title>0</title>
<polygon fill="none" stroke="black" points="338.5,-261 186.5,-261 186.5,-193 338.5,-193 338.5,-261"/>
<text text-anchor="middle" x="262.5" y="-245.8" font-family="Times,serif" font-size="14.0">color_intensity &lt;= 3.8</text>
<text text-anchor="middle" x="262.5" y="-230.8" font-family="Times,serif" font-size="14.0">c_gini = 89.6</text>
<text text-anchor="middle" x="262.5" y="-215.8" font-family="Times,serif" font-size="14.0">instances = 136</text>
<text text-anchor="middle" x="262.5" y="-200.8" font-family="Times,serif" font-size="14.0">counts = [45, 54, 37]</text>
<title>1</title>
<polygon fill="none" stroke="black" points="251,-157 132,-157 132,-89 251,-89 251,-157"/>
<text text-anchor="middle" x="191.5" y="-141.8" font-family="Times,serif" font-size="14.0">ash &lt;= 3.0</text>
<text text-anchor="middle" x="191.5" y="-126.8" font-family="Times,serif" font-size="14.0">c_gini = 3.8</text>
<text text-anchor="middle" x="191.5" y="-111.8" font-family="Times,serif" font-size="14.0">instances = 49</text>
<text text-anchor="middle" x="191.5" y="-96.8" font-family="Times,serif" font-size="14.0">counts = [2, 47, 0]</text>
</g>
<g class="edge"><title>0&#45;&gt;1</title>
<path fill="none" stroke="black" d="M239.4,-192.9C233.4,-184.2 226.7,-174.6 220.4,-165.5"/>
<polygon fill="black" stroke="black" points="223.3,-163.5 214.7,-157.3 217.5,-167.5 223.3,-163.5"/>
</g>
<g class="node"><title>5</title>
<polygon fill="none" stroke="black" points="397.5,-157 269.5,-157 269.5,-89 397.5,-89 397.5,-157"/>
<text text-anchor="middle" x="333.5" y="-141.8" font-family="Times,serif" font-size="14.0">flavanoids &lt;= 1.6</text>
<text text-anchor="middle" x="333.5" y="-126.8" font-family="Times,serif" font-size="14.0">c_gini = 49.5</text>
<text text-anchor="middle" x="333.5" y="-111.8" font-family="Times,serif" font-size="14.0">instances = 87</text>
<text text-anchor="middle" x="333.5" y="-96.8" font-family="Times,serif" font-size="14.0">counts = [43, 7, 37]</text>
</g>
<g class="edge"><title>0&#45;&gt;5</title>
<path fill="none" stroke="black" d="M285.6,-192.9C291.6,-184.2 298.3,-174.6 304.6,-165.5"/>
<polygon fill="black" stroke="black" points="307.5,-167.5 310.3,-157.3 301.7,-163.5 307.5,-167.5"/>
</g>
<g class="node"><title>2</title>
<polygon fill="none" stroke="black" points="119,-53 0,-53 0,-0 119,-0 119,-53"/>
<text text-anchor="middle" x="59.5" y="-37.8" font-family="Times,serif" font-size="14.0">c_gini = 2.0</text>
<text text-anchor="middle" x="59.5" y="-22.8" font-family="Times,serif" font-size="14.0">instances = 48</text>
<text text-anchor="middle" x="59.5" y="-7.8" font-family="Times,serif" font-size="14.0">counts = [1, 47, 0]</text>
</g>
<g class="edge"><title>1&#45;&gt;2</title>
<path fill="none" stroke="black" d="M145.3,-88.9C131.8,-79.3 117.0,-68.7 103.6,-59.1"/>
<polygon fill="black" stroke="black" points="105.6,-56.2 95.4,-53.2 101.5,-61.9 105.6,-56.2"/>
</g>
<g class="node"><title>3</title>
<polygon fill="none" stroke="black" points="249.5,-53 137.5,-53 137.5,-0 249.5,-0 249.5,-53"/>
<text text-anchor="middle" x="193.5" y="-37.8" font-family="Times,serif" font-size="14.0">c_gini = 0.0</text>
<text text-anchor="middle" x="193.5" y="-22.8" font-family="Times,serif" font-size="14.0">instances = 1</text>
<text text-anchor="middle" x="193.5" y="-7.8" font-family="Times,serif" font-size="14.0">counts = [1, 0, 0]</text>
</g>
<g class="edge"><title>1&#45;&gt;3</title>
<path fill="none" stroke="black" d="M192.2,-88.9C192.4,-80.7 192.6,-71.8 192.7,-63.5"/>
<polygon fill="black" stroke="black" points="196.2,-63.3 193.0,-53.2 189.2,-63.2 196.2,-63.3"/>
</g>
<g class="node"><title>6</title>
<polygon fill="none" stroke="black" points="391,-53 272,-53 272,-0 391,-0 391,-53"/>
<text text-anchor="middle" x="331.5" y="-37.8" font-family="Times,serif" font-size="14.0">c_gini = 1.9</text>
<text text-anchor="middle" x="331.5" y="-22.8" font-family="Times,serif" font-size="14.0">instances = 38</text>
<text text-anchor="middle" x="331.5" y="-7.8" font-family="Times,serif" font-size="14.0">counts = [0, 1, 37]</text>
</g>
<g class="edge"><title>5&#45;&gt;6</title>
<path fill="none" stroke="black" d="M332.8,-88.9C332.6,-80.7 332.4,-71.8 332.3,-63.5"/>
<polygon fill="black" stroke="black" points="335.8,-63.2 332.0,-53.2 328.8,-63.3 335.8,-63.2"/>
</g>
<g class="node"><title>7</title>
<polygon fill="none" stroke="black" points="528,-53 409,-53 409,-0 528,-0 528,-53"/>
<text text-anchor="middle" x="468.5" y="-37.8" font-family="Times,serif" font-size="14.0">c_gini = 10.5</text>
<text text-anchor="middle" x="468.5" y="-22.8" font-family="Times,serif" font-size="14.0">instances = 49</text>
<text text-anchor="middle" x="468.5" y="-7.8" font-family="Times,serif" font-size="14.0">counts = [43, 6, 0]</text>
</g>
<g class="edge"><title>5&#45;&gt;7</title>
<path fill="none" stroke="black" d="M380.7,-88.9C394.6,-79.3 409.7,-68.7 423.4,-59.1"/>
<polygon fill="black" stroke="black" points="425.5,-61.8 431.7,-53.2 421.5,-56.1 425.5,-61.8"/>
</g>
</g>
</svg>

- `--criterion=gini --min_to_split=49 --seed=42`
```
Train acc: 97.8%
Test acc: 95.2%
```
<svg width="605pt" height="373pt" viewBox="0.0 0.0 605.0 373.0" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g class="graph" transform="scale(1 1) rotate(0) translate(4 369)">
<title>Tree</title>
<polygon fill="none" stroke="none" points="-4,4 -4,-369 601,-369 601,4 -4,4"/>
<g class="node"><title>0</title>
<polygon fill="none" stroke="black" points="338.5,-365 186.5,-365 186.5,-297 338.5,-297 338.5,-365"/>
<text text-anchor="middle" x="262.5" y="-349.8" font-family="Times,serif" font-size="14.0">color_intensity &lt;= 3.8</text>
<text text-anchor="middle" x="262.5" y="-334.8" font-family="Times,serif" font-size="14.0">c_gini = 89.6</text>
<text text-anchor="middle" x="262.5" y="-319.8" font-family="Times,serif" font-size="14.0">instances = 136</text>
<text text-anchor="middle" x="262.5" y="-304.8" font-family="Times,serif" font-size="14.0">counts = [45, 54, 37]</text>
<title>1</title>
<polygon fill="none" stroke="black" points="251,-261 132,-261 132,-193 251,-193 251,-261"/>
<text text-anchor="middle" x="191.5" y="-245.8" font-family="Times,serif" font-size="14.0">ash &lt;= 3.0</text>
<text text-anchor="middle" x="191.5" y="-230.8" font-family="Times,serif" font-size="14.0">c_gini = 3.8</text>
<text text-anchor="middle" x="191.5" y="-215.8" font-family="Times,serif" font-size="14.0">instances = 49</text>
<text text-anchor="middle" x="191.5" y="-200.8" font-family="Times,serif" font-size="14.0">counts = [2, 47, 0]</text>
</g>
<g class="edge"><title>0&#45;&gt;1</title>
<path fill="none" stroke="black" d="M239.4,-296.9C233.4,-288.2 226.7,-278.6 220.4,-269.5"/>
<polygon fill="black" stroke="black" points="223.3,-267.5 214.7,-261.3 217.5,-271.5 223.3,-267.5"/>
</g>
<g class="node"><title>5</title>
<polygon fill="none" stroke="black" points="397.5,-261 269.5,-261 269.5,-193 397.5,-193 397.5,-261"/>
<text text-anchor="middle" x="333.5" y="-245.8" font-family="Times,serif" font-size="14.0">flavanoids &lt;= 1.6</text>
<text text-anchor="middle" x="333.5" y="-230.8" font-family="Times,serif" font-size="14.0">c_gini = 49.5</text>
<text text-anchor="middle" x="333.5" y="-215.8" font-family="Times,serif" font-size="14.0">instances = 87</text>
<text text-anchor="middle" x="333.5" y="-200.8" font-family="Times,serif" font-size="14.0">counts = [43, 7, 37]</text>
</g>
<g class="edge"><title>0&#45;&gt;5</title>
<path fill="none" stroke="black" d="M285.6,-296.9C291.6,-288.2 298.3,-278.6 304.6,-269.5"/>
<polygon fill="black" stroke="black" points="307.5,-271.5 310.3,-261.3 301.7,-267.5 307.5,-271.5"/>
</g>
<g class="node"><title>2</title>
<polygon fill="none" stroke="black" points="119,-149.5 0,-149.5 0,-96.5 119,-96.5 119,-149.5"/>
<text text-anchor="middle" x="59.5" y="-134.3" font-family="Times,serif" font-size="14.0">c_gini = 2.0</text>
<text text-anchor="middle" x="59.5" y="-119.3" font-family="Times,serif" font-size="14.0">instances = 48</text>
<text text-anchor="middle" x="59.5" y="-104.3" font-family="Times,serif" font-size="14.0">counts = [1, 47, 0]</text>
</g>
<g class="edge"><title>1&#45;&gt;2</title>
<path fill="none" stroke="black" d="M148.6,-192.9C133.3,-181.0 116.0,-167.6 100.8,-155.9"/>
<polygon fill="black" stroke="black" points="102.6,-152.9 92.5,-149.5 98.3,-158.4 102.6,-152.9"/>
</g>
<g class="node"><title>3</title>
<polygon fill="none" stroke="black" points="249.5,-149.5 137.5,-149.5 137.5,-96.5 249.5,-96.5 249.5,-149.5"/>
<text text-anchor="middle" x="193.5" y="-134.3" font-family="Times,serif" font-size="14.0">c_gini = 0.0</text>
<text text-anchor="middle" x="193.5" y="-119.3" font-family="Times,serif" font-size="14.0">instances = 1</text>
<text text-anchor="middle" x="193.5" y="-104.3" font-family="Times,serif" font-size="14.0">counts = [1, 0, 0]</text>
</g>
<g class="edge"><title>1&#45;&gt;3</title>
<path fill="none" stroke="black" d="M192.1,-192.9C192.4,-182.2 192.6,-170.4 192.8,-159.5"/>
<polygon fill="black" stroke="black" points="196.3,-159.6 193,-149.5 189.3,-159.4 196.3,-159.6"/>
</g>
<g class="node"><title>6</title>
<polygon fill="none" stroke="black" points="391,-149.5 272,-149.5 272,-96.5 391,-96.5 391,-149.5"/>
<text text-anchor="middle" x="331.5" y="-134.3" font-family="Times,serif" font-size="14.0">c_gini = 1.9</text>
<text text-anchor="middle" x="331.5" y="-119.3" font-family="Times,serif" font-size="14.0">instances = 38</text>
<text text-anchor="middle" x="331.5" y="-104.3" font-family="Times,serif" font-size="14.0">counts = [0, 1, 37]</text>
</g>
<g class="edge"><title>5&#45;&gt;6</title>
<path fill="none" stroke="black" d="M332.9,-192.9C332.6,-182.2 332.4,-170.4 332.2,-159.5"/>
<polygon fill="black" stroke="black" points="335.7,-159.4 332,-149.5 328.7,-159.6 335.7,-159.4"/>
</g>
<g class="node"><title>7</title>
<polygon fill="none" stroke="black" points="532,-157 409,-157 409,-89 532,-89 532,-157"/>
<text text-anchor="middle" x="470.5" y="-141.8" font-family="Times,serif" font-size="14.0">proline &lt;= 724.5</text>
<text text-anchor="middle" x="470.5" y="-126.8" font-family="Times,serif" font-size="14.0">c_gini = 10.5</text>
<text text-anchor="middle" x="470.5" y="-111.8" font-family="Times,serif" font-size="14.0">instances = 49</text>
<text text-anchor="middle" x="470.5" y="-96.8" font-family="Times,serif" font-size="14.0">counts = [43, 6, 0]</text>
</g>
<g class="edge"><title>5&#45;&gt;7</title>
<path fill="none" stroke="black" d="M378.0,-192.9C390.7,-183.4 404.6,-173.1 417.7,-163.3"/>
<polygon fill="black" stroke="black" points="419.8,-166.1 425.8,-157.3 415.7,-160.5 419.8,-166.1"/>
</g>
<g class="node"><title>8</title>
<polygon fill="none" stroke="black" points="459.5,-53 347.5,-53 347.5,-0 459.5,-0 459.5,-53"/>
<text text-anchor="middle" x="403.5" y="-37.8" font-family="Times,serif" font-size="14.0">c_gini = 1.7</text>
<text text-anchor="middle" x="403.5" y="-22.8" font-family="Times,serif" font-size="14.0">instances = 7</text>
<text text-anchor="middle" x="403.5" y="-7.8" font-family="Times,serif" font-size="14.0">counts = [1, 6, 0]</text>
</g>
<g class="edge"><title>7&#45;&gt;8</title>
<path fill="none" stroke="black" d="M447.1,-88.9C440.8,-80.1 434.0,-70.5 427.6,-61.5"/>
<polygon fill="black" stroke="black" points="430.4,-59.4 421.7,-53.2 424.7,-63.4 430.4,-59.4"/>
</g>
<g class="node"><title>9</title>
<polygon fill="none" stroke="black" points="597,-53 478,-53 478,-0 597,-0 597,-53"/>
<text text-anchor="middle" x="537.5" y="-37.8" font-family="Times,serif" font-size="14.0">c_gini = 0.0</text>
<text text-anchor="middle" x="537.5" y="-22.8" font-family="Times,serif" font-size="14.0">instances = 42</text>
<text text-anchor="middle" x="537.5" y="-7.8" font-family="Times,serif" font-size="14.0">counts = [42, 0, 0]</text>
</g>
<g class="edge"><title>7&#45;&gt;9</title>
<path fill="none" stroke="black" d="M493.9,-88.9C500.2,-80.1 507.0,-70.5 513.4,-61.5"/>
<polygon fill="black" stroke="black" points="516.3,-63.4 519.3,-53.2 510.6,-59.4 516.3,-63.4"/>
</g>
</g>
</svg>

- `--criterion=gini --max_leaves=4 --seed=42`
```
Train acc: 97.1%
Test acc: 95.2%
```
<svg width="405pt" height="373pt" viewBox="0.0 0.0 405.0 373.0" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g class="graph" transform="scale(1 1) rotate(0) translate(4 369)">
<title>Tree</title>
<polygon fill="none" stroke="none" points="-4,4 -4,-369 401,-369 401,4 -4,4"/>
<g class="node"><title>0</title>
<polygon fill="none" stroke="black" points="206.5,-365 54.5,-365 54.5,-297 206.5,-297 206.5,-365"/>
<text text-anchor="middle" x="130.5" y="-349.8" font-family="Times,serif" font-size="14.0">color_intensity &lt;= 3.8</text>
<text text-anchor="middle" x="130.5" y="-334.8" font-family="Times,serif" font-size="14.0">c_gini = 89.6</text>
<text text-anchor="middle" x="130.5" y="-319.8" font-family="Times,serif" font-size="14.0">instances = 136</text>
<text text-anchor="middle" x="130.5" y="-304.8" font-family="Times,serif" font-size="14.0">counts = [45, 54, 37]</text>
<title>1</title>
<polygon fill="none" stroke="black" points="119,-253.5 0,-253.5 0,-200.5 119,-200.5 119,-253.5"/>
<text text-anchor="middle" x="59.5" y="-238.3" font-family="Times,serif" font-size="14.0">c_gini = 3.8</text>
<text text-anchor="middle" x="59.5" y="-223.3" font-family="Times,serif" font-size="14.0">instances = 49</text>
<text text-anchor="middle" x="59.5" y="-208.3" font-family="Times,serif" font-size="14.0">counts = [2, 47, 0]</text>
</g>
<g class="edge"><title>0&#45;&gt;1</title>
<path fill="none" stroke="black" d="M107.4,-296.9C99.6,-285.7 90.9,-273.1 83.1,-261.9"/>
<polygon fill="black" stroke="black" points="85.8,-259.7 77.3,-253.5 80.1,-263.7 85.8,-259.7"/>
</g>
<g class="node"><title>2</title>
<polygon fill="none" stroke="black" points="265.5,-261 137.5,-261 137.5,-193 265.5,-193 265.5,-261"/>
<text text-anchor="middle" x="201.5" y="-245.8" font-family="Times,serif" font-size="14.0">flavanoids &lt;= 1.6</text>
<text text-anchor="middle" x="201.5" y="-230.8" font-family="Times,serif" font-size="14.0">c_gini = 49.5</text>
<text text-anchor="middle" x="201.5" y="-215.8" font-family="Times,serif" font-size="14.0">instances = 87</text>
<text text-anchor="middle" x="201.5" y="-200.8" font-family="Times,serif" font-size="14.0">counts = [43, 7, 37]</text>
</g>
<g class="edge"><title>0&#45;&gt;2</title>
<path fill="none" stroke="black" d="M153.6,-296.9C159.6,-288.2 166.3,-278.6 172.6,-269.5"/>
<polygon fill="black" stroke="black" points="175.5,-271.5 178.3,-261.3 169.7,-267.5 175.5,-271.5"/>
</g>
<g class="node"><title>3</title>
<polygon fill="none" stroke="black" points="191,-149.5 72,-149.5 72,-96.5 191,-96.5 191,-149.5"/>
<text text-anchor="middle" x="131.5" y="-134.3" font-family="Times,serif" font-size="14.0">c_gini = 1.9</text>
<text text-anchor="middle" x="131.5" y="-119.3" font-family="Times,serif" font-size="14.0">instances = 38</text>
<text text-anchor="middle" x="131.5" y="-104.3" font-family="Times,serif" font-size="14.0">counts = [0, 1, 37]</text>
</g>
<g class="edge"><title>2&#45;&gt;3</title>
<path fill="none" stroke="black" d="M178.8,-192.9C171.1,-181.7 162.5,-169.1 154.7,-157.9"/>
<polygon fill="black" stroke="black" points="157.6,-155.8 149.0,-149.5 151.8,-159.7 157.6,-155.8"/>
</g>
<g class="node"><title>4</title>
<polygon fill="none" stroke="black" points="332,-157 209,-157 209,-89 332,-89 332,-157"/>
<text text-anchor="middle" x="270.5" y="-141.8" font-family="Times,serif" font-size="14.0">proline &lt;= 724.5</text>
<text text-anchor="middle" x="270.5" y="-126.8" font-family="Times,serif" font-size="14.0">c_gini = 10.5</text>
<text text-anchor="middle" x="270.5" y="-111.8" font-family="Times,serif" font-size="14.0">instances = 49</text>
<text text-anchor="middle" x="270.5" y="-96.8" font-family="Times,serif" font-size="14.0">counts = [43, 6, 0]</text>
</g>
<g class="edge"><title>2&#45;&gt;4</title>
<path fill="none" stroke="black" d="M223.9,-192.9C229.7,-184.2 236.1,-174.8 242.2,-165.8"/>
<polygon fill="black" stroke="black" points="245.3,-167.5 248.0,-157.3 239.5,-163.6 245.3,-167.5"/>
</g>
<g class="node"><title>5</title>
<polygon fill="none" stroke="black" points="259.5,-53 147.5,-53 147.5,-0 259.5,-0 259.5,-53"/>
<text text-anchor="middle" x="203.5" y="-37.8" font-family="Times,serif" font-size="14.0">c_gini = 1.7</text>
<text text-anchor="middle" x="203.5" y="-22.8" font-family="Times,serif" font-size="14.0">instances = 7</text>
<text text-anchor="middle" x="203.5" y="-7.8" font-family="Times,serif" font-size="14.0">counts = [1, 6, 0]</text>
</g>
<g class="edge"><title>4&#45;&gt;5</title>
<path fill="none" stroke="black" d="M247.1,-88.9C240.8,-80.1 234.0,-70.5 227.6,-61.5"/>
<polygon fill="black" stroke="black" points="230.4,-59.4 221.7,-53.2 224.7,-63.4 230.4,-59.4"/>
</g>
<g class="node"><title>6</title>
<polygon fill="none" stroke="black" points="397,-53 278,-53 278,-0 397,-0 397,-53"/>
<text text-anchor="middle" x="337.5" y="-37.8" font-family="Times,serif" font-size="14.0">c_gini = 0.0</text>
<text text-anchor="middle" x="337.5" y="-22.8" font-family="Times,serif" font-size="14.0">instances = 42</text>
<text text-anchor="middle" x="337.5" y="-7.8" font-family="Times,serif" font-size="14.0">counts = [42, 0, 0]</text>
</g>
<g class="edge"><title>4&#45;&gt;6</title>
<path fill="none" stroke="black" d="M293.9,-88.9C300.2,-80.1 307.0,-70.5 313.4,-61.5"/>
<polygon fill="black" stroke="black" points="316.3,-63.4 319.3,-53.2 310.6,-59.4 316.3,-63.4"/>
</g>
</g>
</svg>

- `--criterion=entropy --max_leaves=5 --seed=42`
```
Train acc: 97.8%
Test acc: 88.1%
```
<svg width="631pt" height="373pt" viewBox="0.0 0.0 630.5 373.0" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g class="graph" transform="scale(1 1) rotate(0) translate(4 369)">
<title>Tree</title>
<polygon fill="none" stroke="none" points="-4,4 -4,-369 626.5,-369 626.5,4 -4,4"/>
<g class="node"><title>0</title>
<polygon fill="none" stroke="black" points="331.5,-365 199.5,-365 199.5,-297 331.5,-297 331.5,-365"/>
<text text-anchor="middle" x="265.5" y="-349.8" font-family="Times,serif" font-size="14.0">flavanoids &lt;= 1.6</text>
<text text-anchor="middle" x="265.5" y="-334.8" font-family="Times,serif" font-size="14.0">c_entropy = 147.8</text>
<text text-anchor="middle" x="265.5" y="-319.8" font-family="Times,serif" font-size="14.0">instances = 136</text>
<text text-anchor="middle" x="265.5" y="-304.8" font-family="Times,serif" font-size="14.0">counts = [45, 54, 37]</text>
<title>1</title>
<polygon fill="none" stroke="black" points="257,-261 132,-261 132,-193 257,-193 257,-261"/>
<text text-anchor="middle" x="194.5" y="-245.8" font-family="Times,serif" font-size="14.0">hue &lt;= 0.9</text>
<text text-anchor="middle" x="194.5" y="-230.8" font-family="Times,serif" font-size="14.0">c_entropy = 27.3</text>
<text text-anchor="middle" x="194.5" y="-215.8" font-family="Times,serif" font-size="14.0">instances = 49</text>
<text text-anchor="middle" x="194.5" y="-200.8" font-family="Times,serif" font-size="14.0">counts = [0, 12, 37]</text>
</g>
<g class="edge"><title>0&#45;&gt;1</title>
<path fill="none" stroke="black" d="M242.4,-296.9C236.4,-288.2 229.7,-278.6 223.4,-269.5"/>
<polygon fill="black" stroke="black" points="226.3,-267.5 217.7,-261.3 220.5,-271.5 226.3,-267.5"/>
</g>
<g class="node"><title>5</title>
<polygon fill="none" stroke="black" points="400,-261 275,-261 275,-193 400,-193 400,-261"/>
<text text-anchor="middle" x="337.5" y="-245.8" font-family="Times,serif" font-size="14.0">alcohol &lt;= 12.8</text>
<text text-anchor="middle" x="337.5" y="-230.8" font-family="Times,serif" font-size="14.0">c_entropy = 60.2</text>
<text text-anchor="middle" x="337.5" y="-215.8" font-family="Times,serif" font-size="14.0">instances = 87</text>
<text text-anchor="middle" x="337.5" y="-200.8" font-family="Times,serif" font-size="14.0">counts = [45, 42, 0]</text>
</g>
<g class="edge"><title>0&#45;&gt;5</title>
<path fill="none" stroke="black" d="M288.9,-296.9C295.0,-288.2 301.8,-278.6 308.2,-269.5"/>
<polygon fill="black" stroke="black" points="311.1,-271.5 314.0,-261.3 305.4,-267.5 311.1,-271.5"/>
</g>
<g class="node"><title>2</title>
<polygon fill="none" stroke="black" points="119,-149.5 0,-149.5 0,-96.5 119,-96.5 119,-149.5"/>
<text text-anchor="middle" x="59.5" y="-134.3" font-family="Times,serif" font-size="14.0">c_entropy = 0.0</text>
<text text-anchor="middle" x="59.5" y="-119.3" font-family="Times,serif" font-size="14.0">instances = 36</text>
<text text-anchor="middle" x="59.5" y="-104.3" font-family="Times,serif" font-size="14.0">counts = [0, 0, 36]</text>
</g>
<g class="edge"><title>1&#45;&gt;2</title>
<path fill="none" stroke="black" d="M150.7,-192.9C134.8,-180.9 116.9,-167.4 101.3,-155.5"/>
<polygon fill="black" stroke="black" points="103.4,-152.8 93.3,-149.5 99.1,-158.3 103.4,-152.8"/>
</g>
<g class="node"><title>3</title>
<polygon fill="none" stroke="black" points="256,-149.5 137,-149.5 137,-96.5 256,-96.5 256,-149.5"/>
<text text-anchor="middle" x="196.5" y="-134.3" font-family="Times,serif" font-size="14.0">c_entropy = 3.5</text>
<text text-anchor="middle" x="196.5" y="-119.3" font-family="Times,serif" font-size="14.0">instances = 13</text>
<text text-anchor="middle" x="196.5" y="-104.3" font-family="Times,serif" font-size="14.0">counts = [0, 12, 1]</text>
</g>
<g class="edge"><title>1&#45;&gt;3</title>
<path fill="none" stroke="black" d="M195.1,-192.9C195.4,-182.2 195.6,-170.4 195.8,-159.5"/>
<polygon fill="black" stroke="black" points="199.3,-159.6 196,-149.5 192.3,-159.4 199.3,-159.6"/>
</g>
<g class="node"><title>6</title>
<polygon fill="none" stroke="black" points="396,-149.5 277,-149.5 277,-96.5 396,-96.5 396,-149.5"/>
<text text-anchor="middle" x="336.5" y="-134.3" font-family="Times,serif" font-size="14.0">c_entropy = 0.0</text>
<text text-anchor="middle" x="336.5" y="-119.3" font-family="Times,serif" font-size="14.0">instances = 37</text>
<text text-anchor="middle" x="336.5" y="-104.3" font-family="Times,serif" font-size="14.0">counts = [0, 37, 0]</text>
</g>
<g class="edge"><title>5&#45;&gt;6</title>
<path fill="none" stroke="black" d="M337.2,-192.9C337.1,-182.3 337.0,-170.6 336.9,-159.9"/>
<polygon fill="black" stroke="black" points="340.3,-159.5 336.8,-149.5 333.3,-159.6 340.3,-159.5"/>
</g>
<g class="node"><title>7</title>
<polygon fill="none" stroke="black" points="585,-157 414,-157 414,-89 585,-89 585,-157"/>
<text text-anchor="middle" x="499.5" y="-141.8" font-family="Times,serif" font-size="14.0">alcalinity_of_ash &lt;= 21.2</text>
<text text-anchor="middle" x="499.5" y="-126.8" font-family="Times,serif" font-size="14.0">c_entropy = 16.2</text>
<text text-anchor="middle" x="499.5" y="-111.8" font-family="Times,serif" font-size="14.0">instances = 50</text>
<text text-anchor="middle" x="499.5" y="-96.8" font-family="Times,serif" font-size="14.0">counts = [45, 5, 0]</text>
</g>
<g class="edge"><title>5&#45;&gt;7</title>
<path fill="none" stroke="black" d="M390.1,-192.9C405.5,-183.2 422.4,-172.6 438.2,-162.6"/>
<polygon fill="black" stroke="black" points="440.3,-165.4 446.9,-157.1 436.6,-159.5 440.3,-165.4"/>
</g>
<g class="node"><title>8</title>
<polygon fill="none" stroke="black" points="492,-53 373,-53 373,-0 492,-0 492,-53"/>
<text text-anchor="middle" x="432.5" y="-37.8" font-family="Times,serif" font-size="14.0">c_entropy = 0.0</text>
<text text-anchor="middle" x="432.5" y="-22.8" font-family="Times,serif" font-size="14.0">instances = 43</text>
<text text-anchor="middle" x="432.5" y="-7.8" font-family="Times,serif" font-size="14.0">counts = [43, 0, 0]</text>
</g>
<g class="edge"><title>7&#45;&gt;8</title>
<path fill="none" stroke="black" d="M476.1,-88.9C469.8,-80.1 463.0,-70.5 456.6,-61.5"/>
<polygon fill="black" stroke="black" points="459.4,-59.4 450.7,-53.2 453.7,-63.4 459.4,-59.4"/>
</g>
<g class="node"><title>9</title>
<polygon fill="none" stroke="black" points="622.5,-53 510.5,-53 510.5,-0 622.5,-0 622.5,-53"/>
<text text-anchor="middle" x="566.5" y="-37.8" font-family="Times,serif" font-size="14.0">c_entropy = 4.2</text>
<text text-anchor="middle" x="566.5" y="-22.8" font-family="Times,serif" font-size="14.0">instances = 7</text>
<text text-anchor="middle" x="566.5" y="-7.8" font-family="Times,serif" font-size="14.0">counts = [2, 5, 0]</text>
</g>
<g class="edge"><title>7&#45;&gt;9</title>
<path fill="none" stroke="black" d="M522.9,-88.9C529.2,-80.1 536.0,-70.5 542.4,-61.5"/>
<polygon fill="black" stroke="black" points="545.3,-63.4 548.3,-53.2 539.6,-59.4 545.3,-63.4"/>
</g>
</g>
</svg>
