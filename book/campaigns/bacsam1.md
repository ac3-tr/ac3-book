---
authors: Laura Köhler
---

# BACSAM I 2022
## Turbulence and aerosol in situ aircraft observations in the Arctic with Polar 6 and T-Bird

The BACSAM I aircraft campaign with Polar 6 and T-Bird took place from 26 September to 19 October, 2022. It was based in Longyearbyen, Svalbard. The Polar 6 was equipped with aerosol and turbulence instrumentation. 

## Flight tracks

![image](.figures/BACSAM1_flighttracks.png)

The figure shows the eleven research flight during BACSAM I with the color denoting the flight altitude. All flights took place in the vicinity of Svalbard. The last panel shows all flights together. 

## Instrumentation

Included instruments in this repository are:
- 100 Hz meteorology from noseboom
- 100 Hz meteorology from T-Bird
- Partector T-Bird
- Irradiance Polar 6
- KT19 Polar 6

## Processing

All data were processed with the polair package [1]. This repository also contains a notebook for quicklooks (notebooks/Quicklooks_bacsam2.ipynb). The turbulence calibration steps are preformed in notebooks/Manual_processing_steps_bacsam2.ipynb.

To process all flights at once, use
```
for f in 0 1 2 3 4 5 6 7 8; do polair <command> -f $f -c <config>; done
```

[1] Köhler, L. (2026). polair (Version v1.0.4) [Computer software]. https://doi.org/10.5281/zenodo.21703863

## Flight segments

Flight segments are added as an additional coordinate to the data sets called "segment". If you use xarray, you can e.g. use groupby to look at specific segments. Please also note that the wind processing only gives reliable results on straight segments, i.e. not in turns or curves.

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
<td rowspan="2">-1</td>
<td>0</td>
<td>2022-09-20T12:44:30</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2022-09-20T17:23:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="10">0</td>
<td>0</td>
<td>2022-10-03T08:04:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2022-10-03T08:07:00</td>
<td>Slight descent with curves</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2022-10-03T08:16:00</td>
<td>Up and down, curves</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2022-10-03T08:33:30</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2022-10-03T08:35:30</td>
<td>Turn in the middle</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2022-10-03T08:54:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2022-10-03T08:56:00</td>
<td>Curves</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2022-10-03T09:29:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>2022-10-03T09:35:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2022-10-03T09:42:30</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="23">1</td>
<td>0</td>
<td>2022-10-05T07:30:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2022-10-05T07:39:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2022-10-05T07:55:00</td>
<td>Descent</td>
<td>Profile</td>
</tr>
<tr>
<td>3</td>
<td>2022-10-05T08:05:00</td>
<td>Slow descent and turn</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2022-10-05T08:15:00</td>
<td>Ladder leg 1</td>
<td>Very low</td>
</tr>
<tr>
<td>5</td>
<td>2022-10-05T08:29:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2022-10-05T08:35:00</td>
<td>Ladder leg 2</td>
<td>Low leg</td>
</tr>
<tr>
<td>7</td>
<td>2022-10-05T08:45:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>2022-10-05T08:53:00</td>
<td>Ladder leg 3</td>
<td>Slightly higher leg</td>
</tr>
<tr>
<td>9</td>
<td>2022-10-05T09:07:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2022-10-05T09:13:00</td>
<td>Ladder leg 4</td>
<td>Lower middle leg</td>
</tr>
<tr>
<td>11</td>
<td>2022-10-05T09:23:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>2022-10-05T09:27:00</td>
<td>Ladder leg 5</td>
<td>Middle leg</td>
</tr>
<tr>
<td>13</td>
<td>2022-10-05T09:38:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2022-10-05T09:47:00</td>
<td>Ladder leg 6</td>
<td>Higher middle leg</td>
</tr>
<tr>
<td>15</td>
<td>2022-10-05T10:02:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2022-10-05T10:12:00</td>
<td>Ladder leg 7</td>
<td>Lower high leg</td>
</tr>
<tr>
<td>17</td>
<td>2022-10-05T10:22:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>2022-10-05T10:30:00</td>
<td>Ladder leg 8</td>
<td>High leg</td>
</tr>
<tr>
<td>19</td>
<td>2022-10-05T10:40:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>2022-10-05T10:52:00</td>
<td>Ladder leg 9</td>
<td>Highest leg</td>
</tr>
<tr>
<td>21</td>
<td>2022-10-05T11:03:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>22</td>
<td>2022-10-05T11:40:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="25">2</td>
<td>0</td>
<td>2022-10-06T08:01:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2022-10-06T08:12:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2022-10-06T08:30:00</td>
<td>Descent</td>
<td>Profile</td>
</tr>
<tr>
<td>3</td>
<td>2022-10-06T08:45:00</td>
<td>Low leg</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2022-10-06T08:51:30</td>
<td>Turn and descent</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2022-10-06T09:07:00</td>
<td>Low leg</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>6</td>
<td>2022-10-06T09:18:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2022-10-06T09:25:00</td>
<td>Ladder leg 1</td>
<td>Lowest leg, calibration 1</td>
</tr>
<tr>
<td>8</td>
<td>2022-10-06T09:33:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2022-10-06T09:39:30</td>
<td>Ladder leg 2</td>
<td>Low leg</td>
</tr>
<tr>
<td>10</td>
<td>2022-10-06T09:50:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>2022-10-06T09:59:00</td>
<td>Ladder leg 3</td>
<td>Higher low leg</td>
</tr>
<tr>
<td>12</td>
<td>2022-10-06T10:08:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>2022-10-06T10:14:00</td>
<td>Ladder leg 4</td>
<td>Lower middle leg, calibration 2</td>
</tr>
<tr>
<td>14</td>
<td>2022-10-06T10:23:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>2022-10-06T10:29:00</td>
<td>Ladder leg 4</td>
<td>Lower middle leg, calibration 2</td>
</tr>
<tr>
<td>16</td>
<td>2022-10-06T10:37:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>2022-10-06T10:49:30</td>
<td>Ladder leg 5</td>
<td>Middle leg, calibration 3</td>
</tr>
<tr>
<td>18</td>
<td>2022-10-06T11:00:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>2022-10-06T11:05:00</td>
<td>Ladder leg 5</td>
<td>Middle leg, calibration 3</td>
</tr>
<tr>
<td>20</td>
<td>2022-10-06T11:13:00</td>
<td>Turn and ascent</td>
<td>Profile</td>
</tr>
<tr>
<td>21</td>
<td>2022-10-06T11:24:00</td>
<td>Ladder leg 6</td>
<td>High leg</td>
</tr>
<tr>
<td>22</td>
<td>2022-10-06T11:34:30</td>
<td>Descent and transit</td>
<td></td>
</tr>
<tr>
<td>23</td>
<td>2022-10-06T12:01:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>24</td>
<td>2022-10-06T12:34:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="19">3</td>
<td>0</td>
<td>2022-10-09T07:50:20</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2022-10-09T07:52:30</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2022-10-09T08:15:30</td>
<td>Middle leg</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2022-10-09T08:21:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2022-10-09T08:24:00</td>
<td>Middle leg</td>
<td>Large roll values</td>
</tr>
<tr>
<td>5</td>
<td>2022-10-09T08:30:00</td>
<td>Middle leg</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>6</td>
<td>2022-10-09T08:35:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2022-10-09T08:39:00</td>
<td>Middle leg</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>8</td>
<td>2022-10-09T08:48:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2022-10-09T08:50:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2022-10-09T08:59:00</td>
<td>Higher leg</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>2022-10-09T09:05:00</td>
<td>Turn and curves</td>
<td>Large roll values</td>
</tr>
<tr>
<td>12</td>
<td>2022-10-09T09:15:30</td>
<td>Middle leg out</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>13</td>
<td>2022-10-09T09:20:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2022-10-09T09:22:00</td>
<td>Middle leg ret</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>15</td>
<td>2022-10-09T09:31:00</td>
<td>Turn, curves, descent</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2022-10-09T09:42:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>2022-10-09T10:08:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>2022-10-09T10:25:50</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="17">4</td>
<td>0</td>
<td>2022-10-11T07:56:30</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2022-10-11T08:00:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2022-10-11T08:08:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2022-10-11T08:14:30</td>
<td>Ascent and curve</td>
<td>Profile</td>
</tr>
<tr>
<td>4</td>
<td>2022-10-11T08:22:00</td>
<td>Descent and curve</td>
<td>Profile</td>
</tr>
<tr>
<td>5</td>
<td>2022-10-11T08:34:30</td>
<td>Straight</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2022-10-11T08:42:00</td>
<td>Descent and turn</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2022-10-11T08:45:00</td>
<td>Ladder leg 1</td>
<td>Lowest leg</td>
</tr>
<tr>
<td>8</td>
<td>2022-10-11T08:54:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2022-10-11T08:58:00</td>
<td>Ladder leg 2</td>
<td>Low leg</td>
</tr>
<tr>
<td>10</td>
<td>2022-10-11T09:10:30</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>2022-10-11T09:17:30</td>
<td>Ladder leg 3</td>
<td>Middle leg</td>
</tr>
<tr>
<td>12</td>
<td>2022-10-11T09:26:30</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>2022-10-11T09:31:00</td>
<td>Ladder leg 4</td>
<td>Highest leg</td>
</tr>
<tr>
<td>14</td>
<td>2022-10-11T09:44:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>2022-10-11T10:06:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2022-10-11T10:10:30</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="14">5</td>
<td>0</td>
<td>2022-10-13T07:46:30</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2022-10-13T07:59:50</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2022-10-13T09:06:00</td>
<td>Descent and turn</td>
<td>Profile</td>
</tr>
<tr>
<td>3</td>
<td>2022-10-13T09:28:00</td>
<td>Low leg out</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>4</td>
<td>2022-10-13T09:39:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2022-10-13T09:47:00</td>
<td>Low leg ret</td>
<td>Calibration 1</td>
</tr>
<tr>
<td>6</td>
<td>2022-10-13T09:57:00</td>
<td>Turn and ascent</td>
<td>Only slightly higher</td>
</tr>
<tr>
<td>7</td>
<td>2022-10-13T10:05:00</td>
<td>Low leg out</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>8</td>
<td>2022-10-13T10:18:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2022-10-13T10:23:00</td>
<td>Low leg ret</td>
<td>Calibration 2</td>
</tr>
<tr>
<td>10</td>
<td>2022-10-13T10:35:00</td>
<td>Ascent</td>
<td>Profile</td>
</tr>
<tr>
<td>11</td>
<td>2022-10-13T10:51:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>2022-10-13T11:32:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>2022-10-13T12:28:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="14">6</td>
<td>0</td>
<td>2022-10-14T08:23:30</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2022-10-14T08:26:30</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2022-10-14T08:32:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>2022-10-14T08:34:00</td>
<td>Curve</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2022-10-14T08:38:00</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2022-10-14T08:39:00</td>
<td>Straight leg</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2022-10-14T08:41:40</td>
<td>Descent and curve</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>2022-10-14T08:46:30</td>
<td>Straight leg</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>2022-10-14T08:51:00</td>
<td>Curve</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2022-10-14T08:52:00</td>
<td>Straight leg</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2022-10-14T08:58:20</td>
<td>Curve</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>2022-10-14T08:59:30</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>2022-10-14T09:08:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>2022-10-14T09:10:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="22">7</td>
<td>0</td>
<td>2022-10-15T07:57:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2022-10-15T08:10:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2022-10-15T09:11:00</td>
<td>Descent and curve</td>
<td>Profile</td>
</tr>
<tr>
<td>3</td>
<td>2022-10-15T09:25:00</td>
<td>Descent and curve</td>
<td>Slower descent</td>
</tr>
<tr>
<td>4</td>
<td>2022-10-15T09:34:00</td>
<td>Ladder leg 1</td>
<td>Low leg 1</td>
</tr>
<tr>
<td>5</td>
<td>2022-10-15T09:45:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>2022-10-15T09:50:00</td>
<td>Ladder leg 2</td>
<td>Low leg 2, calibration 1</td>
</tr>
<tr>
<td>7</td>
<td>2022-10-15T09:59:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>2022-10-15T10:05:00</td>
<td>Ladder leg 3</td>
<td>Low leg 3, calibration 1</td>
</tr>
<tr>
<td>9</td>
<td>2022-10-15T10:13:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2022-10-15T10:18:00</td>
<td>Ladder leg 4</td>
<td>Slightly higher leg out, calibration 2</td>
</tr>
<tr>
<td>11</td>
<td>2022-10-15T10:29:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>2022-10-15T10:35:00</td>
<td>Ladder leg 5</td>
<td>Slightly higher leg ret, calibration 2</td>
</tr>
<tr>
<td>13</td>
<td>2022-10-15T10:44:00</td>
<td>Ascent and turn</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2022-10-15T10:49:00</td>
<td>Ladder leg 6</td>
<td>Middle leg out, calibration 3</td>
</tr>
<tr>
<td>15</td>
<td>2022-10-15T10:57:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2022-10-15T11:02:00</td>
<td>Ladder leg 7</td>
<td>Middle leg ret, calibration 3</td>
</tr>
<tr>
<td>17</td>
<td>2022-10-15T11:08:30</td>
<td>Ascent</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>2022-10-15T11:25:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>2022-10-15T11:43:00</td>
<td>Descent</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>2022-10-15T11:48:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>21</td>
<td>2022-10-15T12:32:00</td>
<td>Landing</td>
<td></td>
</tr>
<tr>
<td rowspan="23">8</td>
<td>0</td>
<td>2022-10-16T07:59:00</td>
<td>Take off</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>2022-10-16T08:06:00</td>
<td>Transit</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2022-10-16T08:33:00</td>
<td>Descent</td>
<td>Profile</td>
</tr>
<tr>
<td>3</td>
<td>2022-10-16T08:40:00</td>
<td>Turn, up and down</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>2022-10-16T08:49:30</td>
<td>Low leg</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>2022-10-16T09:00:00</td>
<td>Ascent and turn</td>
<td>Profile</td>
</tr>
<tr>
<td>6</td>
<td>2022-10-16T09:04:30</td>
<td>Descent and turn</td>
<td>Profile</td>
</tr>
<tr>
<td>7</td>
<td>2022-10-16T09:11:00</td>
<td>Ladder leg 1</td>
<td>Low leg</td>
</tr>
<tr>
<td>8</td>
<td>2022-10-16T09:20:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>2022-10-16T09:25:00</td>
<td>Ladder leg 2</td>
<td>Middle leg</td>
</tr>
<tr>
<td>10</td>
<td>2022-10-16T09:35:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>2022-10-16T09:40:00</td>
<td>Ladder leg 3</td>
<td>High leg</td>
</tr>
<tr>
<td>12</td>
<td>2022-10-16T09:50:00</td>
<td>Straight leg out</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>2022-10-16T10:02:00</td>
<td>Turn</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>2022-10-16T10:07:00</td>
<td>Ladder leg 1</td>
<td>Slightly higher</td>
</tr>
<tr>
<td>15</td>
<td>2022-10-16T10:16:00</td>
<td>Curve and ascent</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>2022-10-16T10:21:00</td>
<td>Curve</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>2022-10-16T10:29:00</td>
<td>Ladder leg 2</td>
<td>Middle leg</td>
</tr>
<tr>
<td>18</td>
<td>2022-10-16T10:39:00</td>
<td>Turn and ascent</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>2022-10-16T10:45:30</td>
<td>Ladder leg 3</td>
<td>High leg</td>
</tr>
<tr>
<td>20</td>
<td>2022-10-16T10:53:00</td>
<td>Transit and descent</td>
<td></td>
</tr>
<tr>
<td>21</td>
<td>2022-10-16T11:37:00</td>
<td>Descent and approach</td>
<td></td>
</tr>
<tr>
<td>22</td>
<td>2022-10-16T11:42:00</td>
<td>Landing</td>
<td></td>
</tr>
</tbody></table>