#ifndef DISTEST_H
#define DISTEST_H

//extern "C" {

namespace hsc {
 namespace meas {
  namespace match {
	void getDistortedPosition(float x_undist, float y_undist, float* x_dist, float* y_dist, float elevation);
	void getUndistortedPosition(float x_dist, float y_dist, float* x_undist, float* y_undist, float elevation);
  }
 }
}

//}
#endif
