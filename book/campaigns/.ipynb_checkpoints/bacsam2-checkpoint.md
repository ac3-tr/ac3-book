---
authors: Laura Köhler
---

# BACSAM II 2024
## Turbulence and aerosol in situ aircraft observations in the Arctic with Polar 6 and T-Bird

Processing documentation for the BACSAM II aircraft campaign with Polar 6 in spring 2024.

To process all flights at once, use
```
for f in 1 2 3 40 41 42 5 6 7 8 9 10 11; do polair <command> -f $f -c <config>; done
```

## Flight segments

<table style="font-size:90%; border-collapse:collapse;">

<thead>
<tr>
<th>Flight</th>
<th>Segment</th>
<th>Time</th>
<th>Type</th>
<th>Comment</th>
</tr>
</thead>
<tbody>

<tr>
<td rowspan="17">1</td>
<td>0</td>
<td>2024-04-07T08:46:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-07T09:00:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-07T09:31:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-07T09:40:00</td>
<td>High leg out</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>4</td>
<td>2024-04-07T09:57:00</td>
<td>Turn and high leg ret</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>5</td>
<td>2024-04-07T10:10:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2024-04-07T10:19:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2024-04-07T10:25:00</td>
<td>Ladder low leg 1 out</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>8</td>
<td>2024-04-07T10:41:00</td>
<td>Ladder low leg 1 ret</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>9</td>
<td>2024-04-07T10:59:00</td>
<td>Ladder middle leg 2 out</td>
<td>Calibration 3</td>
</tr>
<tr>
<td>10</td>
<td>2024-04-07T11:15:30</td>
<td>Ladder middle leg 2 ret</td>
<td>Calibration 3</td>
</tr>
<tr>
<td>11</td>
<td>2024-04-07T11:34:00</td>
<td>Ladder high leg 3 out</td>
<td>Calibration 4</td>
</tr>
<tr>
<td>12</td>
<td>2024-04-07T11:50:00</td>
<td>Ladder high leg 3 ret</td>
<td>Calibration 4</td>
</tr>
<tr>
<td>13</td>
<td>2024-04-07T12:06:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2024-04-07T12:16:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>2024-04-07T12:38:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2024-04-07T12:56:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="20">2</td>
<td>0</td>
<td>2024-04-10T08:28:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-10T08:38:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-10T09:17:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-10T09:30:00</td>
<td>Low straight, ascent and turn</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2024-04-10T09:46:00</td>
<td>Return a bit higher</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2024-04-10T10:07:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2024-04-10T10:12:00</td>
<td>Middle straight, turn</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>7</td>
<td>2024-04-10T10:21:00</td>
<td>Return at same height</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>8</td>
<td>2024-04-10T10:35:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2024-04-10T10:38:00</td>
<td>Straight, a bit lower</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2024-04-10T10:48:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>2024-04-10T10:51:00</td>
<td>Return at height of segment 6 & 7</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>2024-04-10T11:06:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>2024-04-10T11:10:00</td>
<td>Low segment</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2024-04-10T11:27:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>2024-04-10T11:34:00</td>
<td>Straight high segment</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2024-04-10T11:40:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>2024-04-10T11:49:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>2024-04-10T12:10:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>2024-04-10T12:52:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="23">3</td>
<td>0</td>
<td>2024-04-11T08:34:30</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-11T08:38:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-11T09:05:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-11T09:10:00</td>
<td>Ladder leg 1</td>
<td>Low</td>
</tr>
<tr>
<td>4</td>
<td>2024-04-11T09:22:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2024-04-11T09:26:00</td>
<td>Ladder leg 2</td>
<td>Middle</td>
</tr>
<tr>
<td>6</td>
<td>2024-04-11T09:46:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2024-04-11T09:51:00</td>
<td>Ladder leg 3</td>
<td>High</td>
</tr>
<tr>
<td>8</td>
<td>2024-04-11T10:07:00</td>
<td>Descent and change of direction</td>
<td>Profile</td>
</tr>
<tr>
<td>9</td>
<td>2024-04-11T10:13:00</td>
<td>Low straight</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2024-04-11T10:15:00</td>
<td>Ascent</td>
<td>Profile</td>
</tr>
<tr>
<td>11</td>
<td>2024-04-11T10:20:00</td>
<td>Change direction</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>2024-04-11T10:24:00</td>
<td>Ladder leg 1</td>
<td>High</td>
</tr>
<tr>
<td>13</td>
<td>2024-04-11T10:42:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2024-04-11T10:48:00</td>
<td>Ladder leg 2</td>
<td>Middle</td>
</tr>
<tr>
<td>15</td>
<td>2024-04-11T11:06:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2024-04-11T11:09:00</td>
<td>Ladder leg 3, long low segment</td>
<td>Low</td>
</tr>
<tr>
<td>17</td>
<td>2024-04-11T11:43:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>2024-04-11T11:45:00</td>
<td>Straight segment</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>2024-04-11T12:01:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>2024-04-11T12:06:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>21</td>
<td>2024-04-11T12:11:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>22</td>
<td>2024-04-11T12:23:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="4">40</td>
<td>0</td>
<td>2024-04-13T06:11:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-13T06:22:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-13T08:20:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-13T08:38:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="20">41</td>
<td>0</td>
<td>2024-04-13T09:45:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-13T09:49:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-13T09:55:00</td>
<td>Descent</td>
<td>Profile</td>
</tr>
<tr>
<td>3</td>
<td>2024-04-13T10:01:00</td>
<td>Segment 1</td>
<td>Low</td>
</tr>
<tr>
<td>4</td>
<td>2024-04-13T10:22:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2024-04-13T10:23:00</td>
<td>Segment 2</td>
<td>A bit higher</td>
</tr>
<tr>
<td>6</td>
<td>2024-04-13T10:48:30</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2024-04-13T10:52:00</td>
<td>Segment 3</td>
<td>Middle</td>
</tr>
<tr>
<td>8</td>
<td>2024-04-13T11:15:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2024-04-13T11:17:00</td>
<td>Segment 4</td>
<td>High</td>
</tr>
<tr>
<td>10</td>
<td>2024-04-13T11:42:00</td>
<td>Turn and descent</td>
<td>Profile</td>
</tr>
<tr>
<td>11</td>
<td>2024-04-13T11:48:00</td>
<td>Segment 4</td>
<td>Low</td>
</tr>
<tr>
<td>12</td>
<td>2024-04-13T12:13:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>2024-04-13T12:15:00</td>
<td>Segment 3</td>
<td>A bit higher</td>
</tr>
<tr>
<td>14</td>
<td>2024-04-13T12:39:30</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>2024-04-13T12:41:00</td>
<td>Segment 2</td>
<td>Middle</td>
</tr>
<tr>
<td>16</td>
<td>2024-04-13T13:06:30</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>2024-04-13T13:09:00</td>
<td>Segment 1</td>
<td>High</td>
</tr>
<tr>
<td>18</td>
<td>2024-04-13T13:41:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>2024-04-13T13:45:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="4">42</td>
<td>0</td>
<td>2024-04-13T14:29:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-13T14:43:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-13T16:22:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-13T16:45:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="18">5</td>
<td>0</td>
<td>2024-04-15T09:03:46</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-15T09:11:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-15T09:25:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-15T09:30:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2024-04-15T09:55:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2024-04-15T10:00:00</td>
<td>Transit to ladder</td>
<td>Already low</td>
</tr>
<tr>
<td>6</td>
<td>2024-04-15T10:12:40</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2024-04-15T10:15:00</td>
<td>Ladder leg 1</td>
<td>Low</td>
</tr>
<tr>
<td>8</td>
<td>2024-04-15T10:47:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2024-04-15T10:54:00</td>
<td>Ladder leg 2</td>
<td>Middle</td>
</tr>
<tr>
<td>10</td>
<td>2024-04-15T11:25:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>2024-04-15T11:30:30</td>
<td>Ladder leg 3</td>
<td>High</td>
</tr>
<tr>
<td>12</td>
<td>2024-04-15T12:00:00</td>
<td>Descent and turn</td>
<td>Profile</td>
</tr>
<tr>
<td>13</td>
<td>2024-04-15T12:12:30</td>
<td>Ladder leg 4</td>
<td>Low</td>
</tr>
<tr>
<td>14</td>
<td> 2024-04-15T12:43:00</td>
<td>Ascnet</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>2024-04-15T12:51:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2024-04-15T13:27:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>2024-04-15T13:41:13</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="22">6</td>
<td>0</td>
<td>2024-04-17T12:41:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-17T12:52:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-17T13:24:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-17T13:33:00</td>
<td>Straight and turn</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2024-04-17T13:39:00</td>
<td>Ladder leg 1</td>
<td>High</td>
</tr>
<tr>
<td>5</td>
<td>2024-04-17T13:58:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2024-04-17T14:04:00</td>
<td>Ladder leg 2</td>
<td>Middle</td>
</tr>
<tr>
<td>7</td>
<td>2024-04-17T14:24:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>2024-04-17T14:30:00</td>
<td>Ladder leg 3</td>
<td>Low</td>
</tr>
<tr>
<td>9</td>
<td>2024-04-17T14:47:00</td>
<td>Ascent and turn</td>
<td>Profile</td>
</tr>
<tr>
<td>10</td>
<td>2024-04-17T14:54:00</td>
<td>Straight high</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>2024-04-17T14:58:00</td>
<td>Descent and turn</td>
<td>Profile</td>
</tr>
<tr>
<td>12</td>
<td>2024-04-17T15:10:00</td>
<td>Ladder leg 1</td>
<td>Low</td>
</tr>
<tr>
<td>13</td>
<td>2024-04-17T15:29:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2024-04-17T15:33:00</td>
<td>Ladder leg 2</td>
<td>Middle</td>
</tr>
<tr>
<td>15</td>
<td>2024-04-17T15:51:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2024-04-17T15:55:00</td>
<td>Ladder leg 3</td>
<td>High</td>
</tr>
<tr>
<td>17</td>
<td>2024-04-17T16:15:00</td>
<td>Slow ascent and curve</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>2024-04-17T16:22:00</td>
<td>Asent</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>2024-04-17T16:27:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>2024-04-17T17:05:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>21</td>
<td>2024-04-17T17:20:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="21">7</td>
<td>0</td>
<td>2024-04-23T08:27:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-23T08:35:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-23T08:44:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-23T08:48:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2024-04-23T08:56:30</td>
<td>Descent</td>
<td>Probably clouds</td>
</tr>
<tr>
<td>5</td>
<td>2024-04-23T09:13:00</td>
<td>Ascent and descent</td>
<td>Probably clouds</td>
</tr>
<tr>
<td>6</td>
<td>2024-04-23T09:32:00</td>
<td>Ladder leg 1</td>
<td>Low</td>
</tr>
<tr>
<td>7</td>
<td>2024-04-23T09:50:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>2024-04-23T09:57:00</td>
<td>Ladder leg 2</td>
<td>Middle</td>
</tr>
<tr>
<td>9</td>
<td>2024-04-23T10:16:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2024-04-23T10:20:00</td>
<td>Ladder leg 3</td>
<td>High</td>
</tr>
<tr>
<td>11</td>
<td>2024-04-23T10:37:00</td>
<td>Descent and curve</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>2024-04-23T10:41:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>2024-04-23T10:52:00</td>
<td>Ladder leg 1</td>
<td>Middle</td>
</tr>
<tr>
<td>14</td>
<td>2024-04-23T11:16:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>2024-04-23T11:20:00</td>
<td>Ladder leg 2</td>
<td>Low</td>
</tr>
<tr>
<td>16</td>
<td>2024-04-23T11:37:00</td>
<td>Ascent and turn</td>
<td>Profile</td>
</tr>
<tr>
<td>17</td>
<td>2024-04-23T11:45:00</td>
<td>Ladder leg 3</td>
<td>High</td>
</tr>
<tr>
<td>18</td>
<td>2024-04-23T11:58:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>2024-04-23T12:41:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>2024-04-23T12:54:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="33">8</td>
<td>0</td>
<td>2024-04-24T08:26:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-24T08:37:00</td>
<td>Segment 1</td>
<td>Lowest, but not low</td>
</tr>
<tr>
<td>2</td>
<td>2024-04-24T08:53:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-24T08:55:00</td>
<td>Segment 2</td>
<td>Lower middle</td>
</tr>
<tr>
<td>4</td>
<td>2024-04-24T09:00:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2024-04-24T09:03:00</td>
<td>Segment 3</td>
<td>Upper middle</td>
</tr>
<tr>
<td>6</td>
<td>2024-04-24T09:09:30</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2024-04-24T09:11:30</td>
<td>Segment 4</td>
<td>High</td>
</tr>
<tr>
<td>8</td>
<td>2024-04-24T09:21:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2024-04-24T09:29:00</td>
<td>Curve</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2024-04-24T09:33:00</td>
<td>Leg out 1</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>11</td>
<td>2024-04-24T09:43:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>2024-04-24T09:46:30</td>
<td>Leg ret 1</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>13</td>
<td>2024-04-24T09:52:30</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2024-04-24T09:56:00</td>
<td>Leg out 2</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>15</td>
<td>2024-04-24T10:06:30</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2024-04-24T10:09:30</td>
<td>Legt ret 2</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>17</td>
<td>2024-04-24T10:15:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>2024-04-24T10:18:30</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>2024-04-24T10:29:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>2024-04-24T10:35:00</td>
<td>Segment 1</td>
<td></td>
</tr>
<tr>
<td>21</td>
<td>2024-04-24T10:43:00</td>
<td>Segment 2</td>
<td>A little bit lower</td>
</tr>
<tr>
<td>22</td>
<td>2024-04-24T10:51:30</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>23</td>
<td>2024-04-24T10:58:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>24</td>
<td>2024-04-24T11:01:00</td>
<td>Straight segment</td>
<td>Little bit of descent</td>
</tr>
<tr>
<td>25</td>
<td>2024-04-24T11:33:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>26</td>
<td>2024-04-24T11:37:00</td>
<td>Straight</td>
<td>Probably clouds</td>
</tr>
<tr>
<td>27</td>
<td>2024-04-24T11:47:00</td>
<td>Straight</td>
<td></td>
</tr>
<tr>
<td>28</td>
<td>2024-04-24T11:57:00</td>
<td>Curve, them straight</td>
<td></td>
</tr>
<tr>
<td>29</td>
<td>2024-04-24T12:05:30</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>30</td>
<td>2024-04-24T12:13:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>31</td>
<td>2024-04-24T12:36:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>32</td>
<td>2024-04-24T12:56:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="19">9</td>
<td>0</td>
<td>2024-04-25T08:28:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-25T08:37:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-25T08:56:30</td>
<td>Curve and transit</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-25T09:08:00</td>
<td>Descent</td>
<td>Profile</td>
</tr>
<tr>
<td>4</td>
<td>2024-04-25T09:21:00</td>
<td>Leg out 1</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>5</td>
<td>2024-04-25T09:38:30</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2024-04-25T09:42:00</td>
<td>Leg ret 1, Ladder leg 1</td>
<td>Calibration 1, low leg ladder</td>
</tr>
<tr>
<td>7</td>
<td>2024-04-25T10:06:00</td>
<td>Ascent and turn</td>
<td>Profile</td>
</tr>
<tr>
<td>8</td>
<td>2024-04-25T10:12:00</td>
<td>Ladder leg 2</td>
<td>High</td>
</tr>
<tr>
<td>9</td>
<td>2024-04-25T10:33:00</td>
<td>Descent and turn</td>
<td>Probably clouds</td>
</tr>
<tr>
<td>10</td>
<td>2024-04-25T10:45:00</td>
<td>Ladder leg 3</td>
<td>Middle</td>
</tr>
<tr>
<td>11</td>
<td>2024-04-25T10:56:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>2024-04-25T11:01:00</td>
<td>Leg out 2, Ladder leg 4</td>
<td>Calibration 2, low leg ladder</td>
</tr>
<tr>
<td>13</td>
<td>2024-04-25T11:23:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2024-04-25T11:28:00</td>
<td>Leg ret 2</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>15</td>
<td>2024-04-25T11:47:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2024-04-25T11:59:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>2024-04-25T12:13:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>2024-04-25T12:35:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="20">10</td>
<td>0</td>
<td>2024-04-26T08:26:10</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-26T08:38:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-26T09:21:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-26T09:37:00</td>
<td>Curve</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2024-04-26T09:40:00</td>
<td>Ladder leg 1</td>
<td>Middle</td>
</tr>
<tr>
<td>5</td>
<td>2024-04-26T09:58:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2024-04-26T10:02:00</td>
<td>Ladder leg 2</td>
<td>High</td>
</tr>
<tr>
<td>7</td>
<td>2024-04-26T10:33:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>2024-04-26T10:38:00</td>
<td>Ladder 2 leg 1 </td>
<td>Middle</td>
</tr>
<tr>
<td>9</td>
<td>2024-04-26T10:52:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2024-04-26T10:58:00</td>
<td>Ladder 2 leg 2, leg out 1</td>
<td>Low, varying height, calibration 1</td>
</tr>
<tr>
<td>11</td>
<td>2024-04-26T11:29:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>2024-04-26T11:33:00</td>
<td>Leg ret 1</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>13</td>
<td>2024-04-26T11:45:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2024-04-26T11:49:00</td>
<td>Ladder 2 leg 3</td>
<td>Low</td>
</tr>
<tr>
<td>15</td>
<td>2024-04-26T12:07:00</td>
<td>Ascent and curve</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2024-04-26T12:13:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>2024-04-26T12:19:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>2024-04-26T12:41:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>2024-04-26T12:57:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="35">11</td>
<td>0</td>
<td>2024-04-29T10:28:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2024-04-29T10:35:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2024-04-29T10:40:30</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2024-04-29T10:46:00</td>
<td>Segment 1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2024-04-29T10:49:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2024-04-29T10:51:00</td>
<td>Segment 2</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2024-04-29T10:53:00</td>
<td>Turn and segment 3</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2024-04-29T10:58:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>2024-04-29T11:03:00</td>
<td>Segment 4</td>
<td>Low</td>
</tr>
<tr>
<td>9</td>
<td>2024-04-29T11:08:00</td>
<td>Curve</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2024-04-29T11:12:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>2024-04-29T11:16:00</td>
<td>Curve and segment 5</td>
<td>High</td>
</tr>
<tr>
<td>12</td>
<td>2024-04-29T11:21:00</td>
<td>Turn and segment 6</td>
<td>High</td>
</tr>
<tr>
<td>13</td>
<td>2024-04-29T11:28:00</td>
<td>Descent</td>
<td>Profile</td>
</tr>
<tr>
<td>14</td>
<td>2024-04-29T11:30:30</td>
<td>Segment 7</td>
<td>Low</td>
</tr>
<tr>
<td>15</td>
<td>2024-04-29T11:35:00</td>
<td>Segment 8 and curve</td>
<td>Middle</td>
</tr>
<tr>
<td>16</td>
<td>2024-04-29T11:42:00</td>
<td>Segment 9</td>
<td>Low</td>
</tr>
<tr>
<td>17</td>
<td>2024-04-29T11:55:00</td>
<td>Ascent and turn</td>
<td>Profile</td>
</tr>
<tr>
<td>18</td>
<td>2024-04-29T11:59:00</td>
<td>Segment 10</td>
<td>High</td>
</tr>
<tr>
<td>19</td>
<td>2024-04-29T12:07:00</td>
<td>Descent</td>
<td>Profile</td>
</tr>
<tr>
<td>20</td>
<td>2024-04-29T12:10:30</td>
<td>Curve</td>
<td></td>
</tr>
<tr>
<td>21</td>
<td>2024-04-29T12:12:00</td>
<td>Leg out 1</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>22</td>
<td>2024-04-29T12:18:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>23</td>
<td>2024-04-29T12:21:00</td>
<td>Leg ret 1</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>24</td>
<td>2024-04-29T12:26:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>25</td>
<td>2024-04-29T12:29:00</td>
<td>Leg out 2</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>26</td>
<td>2024-04-29T12:37:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>27</td>
<td>2024-04-29T12:40:00</td>
<td>Leg ret 2</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>28</td>
<td>2024-04-29T12:45:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>29</td>
<td>2024-04-29T12:50:00</td>
<td>Straight</td>
<td>Probably clouds</td>
</tr>
<tr>
<td>30</td>
<td>2024-04-29T12:54:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>31</td>
<td>2024-04-29T12:59:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>32</td>
<td>2024-04-29T13:03:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>33</td>
<td>2024-04-29T13:14:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>34</td>
<td>2024-04-29T13:18:30</td>
<td>Landing</td>
<td></td>
</tr>
</tbody></table>

