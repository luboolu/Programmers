<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>개발자가 사용하는 언어와 <code>언어 선호도</code>를 입력하면 그에 맞는 직업군을 추천해주는 알고리즘을 개발하려고 합니다.</p>

<p>아래 표는 5개 직업군 별로 많이 사용하는 5개 언어에 <code>직업군 언어 점수</code>를 부여한 표입니다.</p>
<table class="table">
        <thead><tr>
<th>점수</th>
<th>SI</th>
<th>CONTENTS</th>
<th>HARDWARE</th>
<th>PORTAL</th>
<th>GAME</th>
</tr>
</thead>
        <tbody><tr>
<td>5</td>
<td>JAVA</td>
<td>JAVASCRIPT</td>
<td>C</td>
<td>JAVA</td>
<td>C++</td>
</tr>
<tr>
<td>4</td>
<td>JAVASCRIPT</td>
<td>JAVA</td>
<td>C++</td>
<td>JAVASCRIPT</td>
<td>C#</td>
</tr>
<tr>
<td>3</td>
<td>SQL</td>
<td>PYTHON</td>
<td>PYTHON</td>
<td>PYTHON</td>
<td>JAVASCRIPT</td>
</tr>
<tr>
<td>2</td>
<td>PYTHON</td>
<td>SQL</td>
<td>JAVA</td>
<td>KOTLIN</td>
<td>C</td>
</tr>
<tr>
<td>1</td>
<td>C#</td>
<td>C++</td>
<td>JAVASCRIPT</td>
<td>PHP</td>
<td>JAVA</td>
</tr>
</tbody>
      </table>
<p>예를 들면, SQL의 SI <code>직업군 언어 점수</code>는 3점이지만 CONTENTS <code>직업군 언어 점수</code>는 2점입니다. SQL의 HARDWARE, PORTAL, GAME  <code>직업군 언어 점수</code>는 0점입니다.</p>

<p><code>직업군 언어 점수</code>를 정리한 문자열 배열 <code>table</code>, 개발자가 사용하는 언어를 담은 문자열 배열 <code>languages</code>, <code>언어 선호도</code>를 담은 정수 배열 <code>preference</code>가 매개변수로 주어집니다. 개발자가 사용하는 언어의 <code>언어 선호도</code> x <code>직업군 언어 점수</code>의 총합이 가장 높은 직업군을 return 하도록 solution 함수를 완성해주세요. 총합이 같은 직업군이 여러 개일 경우, 이름이 사전 순으로 가장 빠른 직업군을 return 해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>table</code>의 길이 = 5

<ul>
<li><code>table</code>의 원소는 <code>&quot;직업군 5점언어 4점언어 3점언어 2점언어 1점언어&quot;</code>형식의 문자열입니다. <code>직업군</code>, <code>5점언어</code>, <code>4언어</code>, <code>3점언어</code>, <code>2점언어</code>, <code>1점언어</code>는 하나의 공백으로 구분되어 있습니다.</li>
<li><code>table</code>은 모든 테스트케이스에서 동일합니다.</li>
</ul></li>
<li>1 ≤ <code>languages</code>의 길이 ≤ 9

<ul>
<li><code>languages</code>의 원소는 <code>&quot;JAVA&quot;</code>, <code>&quot;JAVASCRIPT&quot;</code>, <code>&quot;C&quot;</code>, <code>&quot;C++&quot;</code> ,<code>&quot;C#&quot;</code> , <code>&quot;SQL&quot;</code>, <code>&quot;PYTHON&quot;</code>, <code>&quot;KOTLIN&quot;</code>, <code>&quot;PHP&quot;</code> 중 한 개 이상으로 이루어져 있습니다.</li>
<li><code>languages</code>의 원소는 중복되지 않습니다.</li>
</ul></li>
<li><code>preference</code>의 길이 = <code>languages</code>의 길이

<ul>
<li>1 ≤ <code>preference</code>의 원소 ≤ 10</li>
</ul></li>
<li><code>preference</code>의 i번째 원소는 <code>languages</code>의 i번째 원소의 <code>언어 선호도</code>입니다.</li>
<li>return 할 문자열은 <code>&quot;SI&quot;</code>, <code>&quot;CONTENTS&quot;</code>, <code>&quot;HARDWARE&quot;</code>, <code>&quot;PORTAL&quot;</code>, <code>&quot;GAME&quot;</code> 중 하나입니다.<br></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>table</th>
<th>languages</th>
<th>preference</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>[&quot;SI JAVA JAVASCRIPT SQL PYTHON C#&quot;, &quot;CONTENTS JAVASCRIPT JAVA PYTHON SQL C++&quot;, &quot;HARDWARE C C++ PYTHON JAVA JAVASCRIPT&quot;, &quot;PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP&quot;, &quot;GAME C++ C# JAVASCRIPT C JAVA&quot;]</code></td>
<td><code>[&quot;PYTHON&quot;, &quot;C++&quot;, &quot;SQL&quot;]</code></td>
<td>[7, 5, 5]</td>
<td><code>&quot;HARDWARE&quot;</code></td>
</tr>
<tr>
<td><code>[&quot;SI JAVA JAVASCRIPT SQL PYTHON C#&quot;, &quot;CONTENTS JAVASCRIPT JAVA PYTHON SQL C++&quot;, &quot;HARDWARE C C++ PYTHON JAVA JAVASCRIPT&quot;, &quot;PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP&quot;, &quot;GAME C++ C# JAVASCRIPT C JAVA&quot;]</code></td>
<td><code>[&quot;JAVA&quot;, &quot;JAVASCRIPT&quot;]</code></td>
<td>[7, 5]</td>
<td><code>&quot;PORTAL&quot;</code></td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>각 직업군 별로 점수를 계산해보면 아래와 같습니다.</p>

<p>아래 사진은 <code>개발자 언어 선호도</code> 나타낸 표입니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/9a711ad6-4a8e-4028-b100-0280a4e3a7dd/tc1_preference.PNG" title="" alt="tc1_preference.PNG"></p>

<p>아래 사진은 개발자가 선호하는 언어의 <code>직업군 언어 점수</code>를 나타낸 표입니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/1ef5a88a-8109-415d-b611-a6320410b1e1/tc1_score.PNG" title="" alt="tc1_score.PNG"></p>

<p>따라서 점수 총합이 41로 가장 높은 <code>&quot;HARDWARE&quot;</code>를 return 해야 합니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>각 직업군 별로 점수를 계산해보면 아래와 같습니다.</p>

<p>아래 사진은 <code>개발자 언어 선호도</code> 나타낸 표입니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e49d818b-938a-4cc3-8d2a-27783f2e1af5/tc2_preference.PNG" title="" alt="tc2_preference.PNG"></p>

<p>아래 사진은 개발자가 선호하는 언어의 <code>직업군 언어 점수</code>를 나타낸 표입니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/0624156e-e1d3-4299-b554-470815322a79/tc2_score.PNG" title="" alt="tc2_score.PNG"><br>
점수 총합이 55로 가장 높은 직업군은 &quot;SI&quot; 와 &quot;PORTAL&quot;입니다.<br>
따라서 사전 순으로 먼저 오는  <code>&quot;PORTAL&quot;</code>을 return 해야 합니다.</p>
</div>
    </div>