<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>사전에 알파벳 모음 &#39;A&#39;, &#39;E&#39;, &#39;I&#39;, &#39;O&#39;, &#39;U&#39;만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 &quot;A&quot;이고, 그다음은 &quot;AA&quot;이며, 마지막 단어는 &quot;UUUUU&quot;입니다.</p>

<p>단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>word의 길이는 1 이상 5 이하입니다.</li>
<li>word는 알파벳 대문자 &#39;A&#39;, &#39;E&#39;, &#39;I&#39;, &#39;O&#39;, &#39;U&#39;로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>word</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>&quot;AAAAE&quot;</code></td>
<td>6</td>
</tr>
<tr>
<td><code>&quot;AAAE&quot;</code></td>
<td>10</td>
</tr>
<tr>
<td><code>&quot;I&quot;</code></td>
<td>1563</td>
</tr>
<tr>
<td><code>&quot;EIO&quot;</code></td>
<td>1189</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<p>사전에서 첫 번째 단어는 &quot;A&quot;이고, 그다음은 &quot;AA&quot;, &quot;AAA&quot;, &quot;AAAA&quot;, &quot;AAAAA&quot;, &quot;AAAAE&quot;, ... 와 같습니다. &quot;AAAAE&quot;는 사전에서 6번째 단어입니다.</p>

<p>입출력 예 #2</p>

<p>&quot;AAAE&quot;는  &quot;A&quot;, &quot;AA&quot;, &quot;AAA&quot;, &quot;AAAA&quot;, &quot;AAAAA&quot;, &quot;AAAAE&quot;, &quot;AAAAI&quot;, &quot;AAAAO&quot;, &quot;AAAAU&quot;의 다음인 10번째 단어입니다.</p>

<p>입출력 예 #3</p>

<p>&quot;I&quot;는 1563번째 단어입니다.</p>

<p>입출력 예 #4</p>

<p>&quot;EIO&quot;는 1189번째 단어입니다.</p>
</div>
    </div>
