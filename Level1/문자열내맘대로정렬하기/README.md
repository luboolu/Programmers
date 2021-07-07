<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 [&quot;sun&quot;, &quot;bed&quot;, &quot;car&quot;]이고 n이 1이면 각 단어의 인덱스 1의 문자 &quot;u&quot;, &quot;e&quot;, &quot;a&quot;로 strings를 정렬합니다.</p>

<h5>제한 조건</h5>

<ul>
<li>strings는 길이 1 이상, 50이하인 배열입니다.</li>
<li>strings의 원소는 소문자 알파벳으로 이루어져 있습니다.</li>
<li>strings의 원소는 길이 1 이상, 100이하인 문자열입니다.</li>
<li>모든 strings의 원소의 길이는 n보다 큽니다.</li>
<li>인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>strings</th>
<th>n</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[&quot;sun&quot;, &quot;bed&quot;, &quot;car&quot;]</td>
<td>1</td>
<td>[&quot;car&quot;, &quot;bed&quot;, &quot;sun&quot;]</td>
</tr>
<tr>
<td>[&quot;abce&quot;, &quot;abcd&quot;, &quot;cdx&quot;]</td>
<td>2</td>
<td>[&quot;abcd&quot;, &quot;abce&quot;, &quot;cdx&quot;]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p><strong>입출력 예 1</strong><br>
&quot;sun&quot;, &quot;bed&quot;, &quot;car&quot;의 1번째 인덱스 값은 각각 &quot;u&quot;, &quot;e&quot;, &quot;a&quot; 입니다. 이를 기준으로 strings를 정렬하면 [&quot;car&quot;, &quot;bed&quot;, &quot;sun&quot;] 입니다.</p>

<p><strong>입출력 예 2</strong><br>
&quot;abce&quot;와 &quot;abcd&quot;, &quot;cdx&quot;의 2번째 인덱스 값은 &quot;c&quot;, &quot;c&quot;, &quot;x&quot;입니다. 따라서 정렬 후에는 &quot;cdx&quot;가 가장 뒤에 위치합니다. &quot;abce&quot;와 &quot;abcd&quot;는 사전순으로 정렬하면 &quot;abcd&quot;가 우선하므로, 답은 [&quot;abcd&quot;, &quot;abce&quot;, &quot;cdx&quot;] 입니다.</p>
</div>
    </div>
