import json
import logging
logging.basicConfig(level=logging.DEBUG)

def calculate_turbidity(cal_const: float, detec_current: float):
    """
    Given the calibration constant and detector current of a water quality data set, this function will multiply by them
    to obtain the turbidity of such data set, then return the result.

    Args:
        cal_const (float): The calibration constant of a water quality data set.
        detec_current (float): The detector current of a water quality data set.

    Returns:
        T (float): The turbidity of the water quality data set.
    """
    a0 = cal_const         #Calibration Constant
    I90 = detec_current    #Ninety degree detector current
    T = a0 * I90           #Turbidity in NTU Units (0-40)

    return(T)

def safe_threshold_time(turbidity: float):
    """
    Give the turbidity of a water quality data set, this function will compare it to a turbidity threshold for safe water,
    calculate the amount of time elapsed required to return to a safe water turbidity threshold, print out the result, and
    return the elapsed time.

    Args:
        turbidity (float): The turbidity of a water quality data set.

    Returns:
        b (float) = Hours elapsed to return to a safe water turbidity threshold
    """
    Ts = 1.0               #Turbidity threshold for safe water
    T0 = turbidity         #Current turbidity
    d = 0.02               #Decay factor per hour
    if(T0 <= Ts):
        b = 0
        logging.info('Turbidity is below threshold for safe use')
    else:
        logging.warning('Turbidity is above threshold for safe use')
        b = (T0 - Ts) / d

    print('Minimum time required to return below a safe threshold =', b, 'hours')

    return(b)

def avg_turbidity(turb_list: list, start_ind: int):
    """
    Given a list with tubidity values and the desired starting index, this function will calculate the average turbidity
    of the most recent five data points, print out this value, and return the average turbidity for the five data points.

    Args:
        turb_list (list): A list that contains the turbidity values of multiple water quality data sets 
        start_ind (int): Starting index for a list

    Returns:
        avg_turb (float): The average turbidity of the most recent five data points
    """
    end_ind = start_ind + 5
    accumulated_turb = 0
    for i in range(start_ind, end_ind):
        accumulated_turb += turb_list[i]

    avg_turb = accumulated_turb / (end_ind - start_ind)
    print('Average turbidity based on most recent five measurements =', avg_turb, 'NTU')

    return(avg_turb)

def main():
    with open('turbidity_data.json', 'r') as f:
        turb_data = json.load(f)

    turbidity_values = []
    for row in turb_data['turbidity_data']:
        turbidity_values.append(calculate_turbidity(float(row['calibration_constant']), float(row['detector_current'])))

    x = int(len(turb_data['turbidity_data']) / 5)
    for i in range(x):
        starting_ind = (i-1)*5
        curr_turb = avg_turbidity(turbidity_values, starting_ind)
        safe_threshold_time(curr_turb)

if __name__ == '__main__':
    main()
