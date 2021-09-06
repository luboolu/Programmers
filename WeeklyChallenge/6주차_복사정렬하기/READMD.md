<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>복서 선수들의 몸무게 weights와, 복서 선수들의 전적을 나타내는 head2head가 매개변수로 주어집니다. 복서 선수들의 번호를 다음과 같은 순서로 정렬한 후 return 하도록 solution 함수를 완성해주세요.</p>

<ol>
<li>전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.</li>
<li>승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.</li>
<li>자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.</li>
<li>자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.</li>
</ol>

<hr>

<h5>제한사항</h5>

<ul>
<li>weights의 길이는 2 이상 1,000 이하입니다.

<ul>
<li>weights의 모든 값은 45 이상 150 이하의 정수입니다.</li>
<li><code>weights[i]</code> 는 i+1번 복서의 몸무게(kg)를 의미합니다.</li>
</ul></li>
<li>head2head의 길이는 weights의 길이와 같습니다.

<ul>
<li>head2head의 모든 문자열은 길이가 weights의 길이와 동일하며, &#39;N&#39;, &#39;W&#39;, &#39;L&#39;로 이루어진 문자열입니다.</li>
<li><code>head2head[i]</code> 는 i+1번 복서의 전적을 의미하며, <code>head2head[i][j]</code>는 i+1번 복서와 j+1번 복서의 매치 결과를 의미합니다.

<ul>
<li>&#39;N&#39; (None)은 두 복서가 아직 붙어본 적이 없음을 의미합니다.</li>
<li>&#39;W&#39; (Win)는 i+1번 복서가 j+1번 복서를 이겼음을 의미합니다.</li>
<li>&#39;L&#39; (Lose)는 i+1번 복사가 j+1번 복서에게 졌음을 의미합니다.</li>
</ul></li>
<li>임의의 i에 대해서 <code>head2head[i][i]</code> 는 항상 &#39;N&#39;입니다. 자기 자신과 싸울 수는 없기 때문입니다.</li>
<li>임의의 i, j에 대해서 <code>head2head[i][j]</code> = &#39;W&#39; 이면, <code>head2head[j][i]</code> = &#39;L&#39;입니다.</li>
<li>임의의 i, j에 대해서 <code>head2head[i][j]</code> = &#39;L&#39; 이면, <code>head2head[j][i]</code> = &#39;W&#39;입니다.</li>
<li>임의의 i, j에 대해서 <code>head2head[i][j]</code> = &#39;N&#39; 이면, <code>head2head[j][i]</code> = &#39;N&#39;입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>weights</th>
<th>head2head</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>[50,82,75,120]</code></td>
<td><code>[&quot;NLWL&quot;,&quot;WNLL&quot;,&quot;LWNW&quot;,&quot;WWLN&quot;]</code></td>
<td><code>[3,4,1,2]</code></td>
</tr>
<tr>
<td><code>[145,92,86]</code></td>
<td><code>[&quot;NLW&quot;,&quot;WNL&quot;,&quot;LWN&quot;]</code></td>
<td><code>[2,3,1]</code></td>
</tr>
<tr>
<td><code>[60,70,60]</code></td>
<td><code>[&quot;NNN&quot;,&quot;NNN&quot;,&quot;NNN&quot;]</code></td>
<td><code>[2,1,3]</code></td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>다음은 선수들의 정보를 나타낸 표입니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>선수 번호</th>
<th>vs 1번</th>
<th>vs 2번</th>
<th>vs 3번</th>
<th>vs 4번</th>
<th>승률</th>
<th>자기보다 무거운 복서를 이긴 횟수</th>
<th>몸무게</th>
</tr>
</thead>
        <tbody><tr>
<td>1번</td>
<td>-</td>
<td>패배</td>
<td>승리</td>
<td>패배</td>
<td>33.33%</td>
<td>1회</td>
<td>50kg</td>
</tr>
<tr>
<td>2번</td>
<td>승리</td>
<td>-</td>
<td>패배</td>
<td>패배</td>
<td>33.33%</td>
<td>0회</td>
<td>82kg</td>
</tr>
<tr>
<td>3번</td>
<td>패배</td>
<td>승리</td>
<td>-</td>
<td>승리</td>
<td>66.66%</td>
<td>2회</td>
<td>75kg</td>
</tr>
<tr>
<td>4번</td>
<td>승리</td>
<td>승리</td>
<td>패배</td>
<td>-</td>
<td>66.66%</td>
<td>0회</td>
<td>120kg</td>
</tr>
</tbody>
      </table>
<ul>
<li>본문에 서술된 우선순위를 따라 <code>[3,4,1,2]</code> 를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>다음은 선수들의 정보를 나타낸 표입니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>선수 번호</th>
<th>vs 1번</th>
<th>vs 2번</th>
<th>vs 3번</th>
<th>승률</th>
<th>자기보다 무거운 복서를 이긴 횟수</th>
<th>몸무게</th>
</tr>
</thead>
        <tbody><tr>
<td>1번</td>
<td>-</td>
<td>패배</td>
<td>승리</td>
<td>50%</td>
<td>0회</td>
<td>145kg</td>
</tr>
<tr>
<td>2번</td>
<td>승리</td>
<td>-</td>
<td>패배</td>
<td>50%</td>
<td>1회</td>
<td>92kg</td>
</tr>
<tr>
<td>3번</td>
<td>패배</td>
<td>승리</td>
<td>-</td>
<td>50%</td>
<td>1회</td>
<td>86kg</td>
</tr>
</tbody>
      </table>
<ul>
<li>본문에 서술된 우선순위를 따라 <code>[2,3,1]</code> 을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>다음은 선수들의 정보를 나타낸 표입니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>선수 번호</th>
<th>vs 1번</th>
<th>vs 2번</th>
<th>vs 3번</th>
<th>승률</th>
<th>자기보다 무거운 복서를 이긴 횟수</th>
<th>몸무게</th>
</tr>
</thead>
        <tbody><tr>
<td>1번</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0% (무전적)</td>
<td>0회</td>
<td>60kg</td>
</tr>
<tr>
<td>2번</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0% (무전적)</td>
<td>0회</td>
<td>70kg</td>
</tr>
<tr>
<td>3번</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0% (무전적)</td>
<td>0회</td>
<td>60kg</td>
</tr>
</tbody>
      </table>
<ul>
<li>본문에 서술된 우선순위를 따라 <code>[2,1,3]</code> 을 return 합니다.</li>
</ul>
</div>
    </div>
